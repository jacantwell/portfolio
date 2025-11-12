from langchain_community.document_loaders import (
    UnstructuredMarkdownLoader,
    PyPDFLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from pathlib import Path

def load_documents_from_directory(directory: str):
    """Load all markdown and PDF files from a directory with proper metadata"""
    documents = []
    
    # Load markdown files
    print("Loading markdown files...")
    md_files = list(Path(directory).rglob("*.md"))
    for md_path in md_files:
        loader = UnstructuredMarkdownLoader(str(md_path))
        docs = loader.load()
        # Add metadata to each document
        for doc in docs:
            doc.metadata['file_name'] = md_path.name
            doc.metadata['file_type'] = 'markdown'
            doc.metadata['source'] = str(md_path)
            # Add category based on file location
            if 'projects' in str(md_path):
                doc.metadata['category'] = 'project'
            elif 'skills' in str(md_path):
                doc.metadata['category'] = 'skills'
            elif 'cv' in md_path.name.lower():
                doc.metadata['category'] = 'cv'
            else:
                doc.metadata['category'] = 'general'
        documents.extend(docs)
    
    # Load PDF files
    print("Loading PDF files...")
    pdf_files = list(Path(directory).rglob("*.pdf"))
    for pdf_path in pdf_files:
        loader = PyPDFLoader(str(pdf_path))
        docs = loader.load()
        # Add metadata to each document
        for doc in docs:
            doc.metadata['file_name'] = pdf_path.name
            doc.metadata['file_type'] = 'pdf'
            doc.metadata['source'] = str(pdf_path)
            doc.metadata['page'] = doc.metadata.get('page', 0)
            # Add category
            if 'cv' in pdf_path.name.lower() or 'resume' in pdf_path.name.lower():
                doc.metadata['category'] = 'cv'
            else:
                doc.metadata['category'] = 'general'
        documents.extend(docs)
    
    print(f"Loaded {len(documents)} documents total")
    return documents

def build_vector_store():
    print("Starting vector store build...")
    
    # Load all documents
    documents = load_documents_from_directory('.chroma/documents')
    
    if not documents:
        print("No documents found! Check your .chroma/documents directory")
        return
    
    # Print some diagnostics
    print("\nDocument summary:")
    for doc in documents[:3]:  # Show first 3
        print(f"  - {doc.metadata.get('file_name', 'unknown')}: {len(doc.page_content)} chars")
    
    # Split into chunks with better settings
    print("\nSplitting documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,  # Larger chunks for better context
        chunk_overlap=300,  # More overlap to preserve context
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""]  # Split on paragraphs first
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    
    # Show sample chunk with metadata
    if chunks:
        print("\nSample chunk:")
        print(f"File: {chunks[0].metadata.get('file_name', 'unknown')}")
        print(f"Category: {chunks[0].metadata.get('category', 'unknown')}")
        print(f"Content preview: {chunks[0].page_content[:200]}...")
    
    # Create embeddings and vector store
    print("\nCreating embeddings and vector store...")
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=".chroma/chroma_db"
    )
    
    print("\n✓ Vector store saved to .chroma/chroma_db")
    print(f"✓ Indexed {len(chunks)} chunks from {len(documents)} documents")
    return vectorstore

if __name__ == "__main__":
    build_vector_store()