# test_retrieval_improved.py
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
vectorstore = Chroma(
    persist_directory="./chroma/chroma_db",
    embedding_function=embeddings
)

# Test queries with more detail
test_queries = [
    "Python?",
    "Projects",
    "education background?",
    "findkairos",
    "React and Vite?",
    "email?",
    "How many years of professional software engineering experience do you have?"
]

print(f"Total documents in vector store: {vectorstore._collection.count()}\n")

for query in test_queries:
    print(f"\nQuery: {query}")
    print("=" * 70)
    
    # Get results with scores
    results = vectorstore.similarity_search_with_score(query, k=3)
    
    for i, (doc, score) in enumerate(results, 1):
        print(f"\nResult {i} (Score: {score:.3f})")
        print(f"File: {doc.metadata.get('file_name', 'unknown')}")
        print(f"Category: {doc.metadata.get('category', 'unknown')}")
        print(f"Content: {doc.page_content[:300].strip()}...")
        print("-" * 70)

# Also test filtered search
print("\n" + "=" * 70)
print("Testing filtered search (CV only)")
print("=" * 70)

cv_results = vectorstore.similarity_search(
    "What is Jasper's experience?",
    k=2,
    filter={"category": "cv"}
)

for i, doc in enumerate(cv_results, 1):
    print(f"\nCV Result {i}:")
    print(f"File: {doc.metadata.get('file_name', 'unknown')}")
    print(f"Content: {doc.page_content[:300].strip()}...")