from langchain_community.document_loaders import (
    UnstructuredMarkdownLoader,
    PyPDFLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from pathlib import Path
import yaml
import re

def extract_yaml_frontmatter(content: str):
    """Extract YAML frontmatter from markdown content"""
    # Match YAML frontmatter between --- delimiters
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        yaml_content = match.group(1)
        markdown_content = match.group(2)
        try:
            metadata = yaml.safe_load(yaml_content)
            return metadata, markdown_content
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return {}, content
    return {}, content

def sanitize_metadata(metadata: dict) -> dict:
    """Convert metadata values to Chroma-compatible types (str, int, float, bool)"""
    from datetime import date, datetime
    
    sanitized = {}
    for key, value in metadata.items():
        if value is None:
            continue
        elif isinstance(value, (date, datetime)):
            sanitized[key] = value.isoformat()  # Convert dates to ISO string
        elif isinstance(value, (str, int, float, bool)):
            sanitized[key] = value
        elif isinstance(value, (list, tuple)):
            sanitized[key] = ", ".join(str(v) for v in value)
        elif isinstance(value, dict):
            import json
            sanitized[key] = json.dumps(value)
        else:
            sanitized[key] = str(value)
    
    return sanitized

def load_markdown_with_metadata(file_path: Path):
    """Load markdown file and extract YAML frontmatter as metadata"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    yaml_metadata, markdown_content = extract_yaml_frontmatter(content)
    clean_metadata = sanitize_metadata(yaml_metadata) if yaml_metadata else {}
    
    # Create document with both content and metadata
    from langchain_core.documents import Document
    doc = Document(
        page_content=markdown_content,
        metadata={
            'file_name': file_path.name,
            'file_type': 'markdown',
            'source': str(file_path),
            **clean_metadata  # Merge in sanitized YAML metadata
        }
    )
    
    return [doc]

def load_documents_from_directory(directory: str):
    """Load all markdown and PDF files from a directory with proper metadata"""
    documents = []
    
    # Load markdown files with YAML frontmatter support
    print("Loading markdown files...")
    md_files = list(Path(directory).rglob("*.md"))
    for md_path in md_files:
        try:
            docs = load_markdown_with_metadata(md_path)
            print(f"  Loaded {md_path.name}: {docs[0].metadata.get('type', 'unknown')} type")
            documents.extend(docs)
        except Exception as e:
            print(f"  Error loading {md_path.name}: {e}")
    
    # Load PDF files
    print("\nLoading PDF files...")
    pdf_files = list(Path(directory).rglob("*.pdf"))
    for pdf_path in pdf_files:
        try:
            loader = PyPDFLoader(str(pdf_path))
            docs = loader.load()
            # Add metadata to each document
            for doc in docs:
                doc.metadata.update({
                    'file_name': pdf_path.name,
                    'file_type': 'pdf',
                    'source': str(pdf_path),
                    'page': doc.metadata.get('page', 0),
                    'type': 'profile' if 'cv' in pdf_path.name.lower() else 'general'
                })
            documents.extend(docs)
            print(f"  Loaded {pdf_path.name}: {len(docs)} pages")
        except Exception as e:
            print(f"  Error loading {pdf_path.name}: {e}")
    
    print(f"\nLoaded {len(documents)} documents total")
    return documents

def get_chunking_config(doc_type: str):
    """Get appropriate chunking configuration based on document type"""
    configs = {
        'profile': {
            'chunk_size': 2000,  # Larger chunks for CV/profile to keep context
            'chunk_overlap': 400,
        },
        'project': {
            'chunk_size': 1500,  # Medium chunks for project READMEs
            'chunk_overlap': 300,
        },
        'application': {
            'chunk_size': 2500,  # Large chunks for Q&A to keep full answers
            'chunk_overlap': 500,
        },
        'default': {
            'chunk_size': 1500,
            'chunk_overlap': 300,
        }
    }
    return configs.get(doc_type, configs['default'])

def smart_chunk_documents(documents):
    """Chunk documents with type-specific strategies"""
    all_chunks = []
    
    for doc in documents:
        doc_type = doc.metadata.get('type', 'default')
        config = get_chunking_config(doc_type)
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config['chunk_size'],
            chunk_overlap=config['chunk_overlap'],
            length_function=len,
            separators=["\n## ", "\n### ", "\n\n", "\n", ". ", " ", ""]  # Split on headers first
        )
        
        chunks = text_splitter.split_documents([doc])
        all_chunks.extend(chunks)
    
    return all_chunks

def print_metadata_summary(documents):
    """Print summary of metadata found in documents"""
    print("\nMetadata Summary:")
    print("=" * 50)
    
    # Group by type
    types = {}
    technologies = set()
    tags = set()
    
    for doc in documents:
        doc_type = doc.metadata.get('type', 'unknown')
        types[doc_type] = types.get(doc_type, 0) + 1
        
        # Collect technologies if present
        if 'technologies_mentioned' in doc.metadata:
            tech = doc.metadata['technologies_mentioned']
            if isinstance(tech, dict):
                for category, items in tech.items():
                    if isinstance(items, list):
                        technologies.update(items)
        
        # Collect tags if present
        if 'tags' in doc.metadata:
            doc_tags = doc.metadata['tags']
            if isinstance(doc_tags, list):
                tags.update(doc_tags)
    
    print(f"\nDocument Types:")
    for doc_type, count in types.items():
        print(f"  {doc_type}: {count}")
    
    if technologies:
        print(f"\nTechnologies Found: {len(technologies)}")
        print(f"  Sample: {list(technologies)[:10]}")
    
    if tags:
        print(f"\nTags Found: {len(tags)}")
        print(f"  All tags: {sorted(tags)}")

def build_vector_store():
    print("Starting vector store build...")
    print("=" * 50)
    
    # Load all documents
    documents = load_documents_from_directory('./chroma/documents')
    
    if not documents:
        print("No documents found! Check your ./chroma/documents directory")
        return
    
    # Print metadata summary
    print_metadata_summary(documents)
    
    # Split into chunks with smart chunking
    print("\n" + "=" * 50)
    print("Chunking documents...")
    chunks = smart_chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")
    
    # Show sample chunks from different types
    print("\nSample chunks by type:")
    shown_types = set()
    for chunk in chunks:
        chunk_type = chunk.metadata.get('type', 'unknown')
        if chunk_type not in shown_types:
            print(f"\n  {chunk_type.upper()}:")
            print(f"    File: {chunk.metadata.get('file_name', 'unknown')}")
            print(f"    Chunk size: {len(chunk.page_content)} chars")
            print(f"    Content preview: {chunk.page_content[:150]}...")
            shown_types.add(chunk_type)
            if len(shown_types) >= 3:
                break
    
    # Create embeddings and vector store
    print("\n" + "=" * 50)
    print("Creating embeddings and vector store...")
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma/chroma_db",
        collection_metadata={"hnsw:space": "cosine"}  # Use cosine similarity
    )
    
    print("\n" + "=" * 50)
    print("✓ Vector store saved to ./chroma/chroma_db")
    print(f"✓ Indexed {len(chunks)} chunks from {len(documents)} documents")
    
    # Test query to verify metadata filtering works
    print("\nTesting metadata filtering...")
    test_results = vectorstore.similarity_search(
        "Python experience",
        k=2,
        filter={"type": "profile"}
    )
    print(f"  Found {len(test_results)} results with type='profile' filter")
    
    return vectorstore

if __name__ == "__main__":
    build_vector_store()