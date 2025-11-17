from langchain_community.document_loaders import (
    PyPDFLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from pathlib import Path
import yaml
import re
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import time
import os
import hashlib
from tqdm import tqdm

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
    """Convert metadata values to Pinecone-compatible types (str, int, float, bool)"""
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


def generate_chunk_id(chunk, index):
    """Generate a unique, deterministic ID for each chunk"""
    content_hash = hashlib.md5(chunk.page_content.encode()).hexdigest()[:8]
    source = chunk.metadata.get('source', 'unknown')
    source_hash = hashlib.md5(source.encode()).hexdigest()[:8]
    return f"{source_hash}_{index}_{content_hash}"

def prepare_pinecone_vectors(chunks, embeddings_model):
    """
    Generate embeddings and format chunks for Pinecone upsert
    
    Args:
        chunks: List of LangChain Document objects
        embeddings_model: Embeddings model (e.g., GoogleGenerativeAIEmbeddings)
    
    Returns:
        List of tuples (id, embedding, metadata)
    """
    print(f"\nGenerating embeddings for {len(chunks)} chunks...")
    vectors = []
    
    # Extract texts for batch embedding
    texts = [chunk.page_content for chunk in chunks]
    
    # Generate embeddings in batch (more efficient)
    embeddings = embeddings_model.embed_documents(texts)
    
    # Prepare vectors with IDs and metadata
    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vector_id = generate_chunk_id(chunk, idx)
        
        # Prepare metadata - Pinecone supports string, number, boolean, list of strings
        metadata = {
            'text': chunk.page_content[:1000],  # Store first 1000 chars for preview
            'full_text': chunk.page_content,  # Store full text
            **chunk.metadata
        }
        
        vectors.append((vector_id, embedding, metadata))
    
    return vectors

def upsert_to_pinecone(index, vectors, batch_size=100):
    """
    Upsert vectors to Pinecone in batches
    
    Args:
        index: Pinecone index object
        vectors: List of tuples (id, embedding, metadata)
        batch_size: Number of vectors to upsert at once
    """
    print(f"\nUpserting {len(vectors)} vectors to Pinecone...")
    
    for i in tqdm(range(0, len(vectors), batch_size)):
        batch = vectors[i:i + batch_size]
        
        try:
            index.upsert(vectors=batch)
        except Exception as e:
            print(f"\nError upserting batch {i//batch_size + 1}: {e}")
            # Retry logic
            time.sleep(1)
            try:
                index.upsert(vectors=batch)
            except Exception as retry_error:
                print(f"Retry failed: {retry_error}")
                continue
    
    print("\nUpsert complete!")
    
    # Get index stats
    stats = index.describe_index_stats()
    print(f"Total vectors in index: {stats.total_vector_count}")

def main():
    """Main function to orchestrate the entire pipeline"""
    


    # Configuration
    DOCS_DIRECTORY = "./documents"  # Change this to your directory
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    INDEX_NAME = "portfolio"
    EMBEDDING_DIMENSION = 3072  # For Google's gemini-embedding-001 model
    
    # Step 1: Initialize Pinecone
    print("Initializing Pinecone...")
    pc = Pinecone(api_key=PINECONE_API_KEY)
    
    # Step 2: Create or connect to index
    try:
        if INDEX_NAME not in pc.list_indexes().names():
            print(f"Creating new index: {INDEX_NAME}")
            pc.create_index(
                name=INDEX_NAME,
                dimension=EMBEDDING_DIMENSION,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )
            # Wait for index to be ready
            time.sleep(10)
        else:
            print(f"Index {INDEX_NAME} already exists")
    except Exception as e:
        print(f"Index creation note: {e}")
    
    index = pc.Index(INDEX_NAME)
    
    # Step 3: Initialize embeddings model
    print("\nInitializing embeddings model...")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
    )
    
    # Step 4: Load documents
    documents = load_documents_from_directory(DOCS_DIRECTORY)
    
    if not documents:
        print("No documents found!")
        return
    
    # Step 5: Print metadata summary
    print_metadata_summary(documents)
    
    # Step 6: Chunk documents
    print("\nChunking documents...")
    chunks = smart_chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")
    
    # Step 7: Generate embeddings and prepare vectors
    vectors = prepare_pinecone_vectors(chunks, embeddings)
    
    # Step 8: Upsert to Pinecone
    upsert_to_pinecone(index, vectors, batch_size=100)
    
    print("\nPipeline complete!")

if __name__ == "__main__":
    main()