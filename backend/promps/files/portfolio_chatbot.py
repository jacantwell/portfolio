"""
Portfolio Chatbot Implementation
Integrates the system prompt with the vector store for portfolio Q&A
"""

from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
import json

# System prompt - condensed version
SYSTEM_PROMPT = """You are an AI assistant representing Jasper Cantwell, a full-stack software engineer. You respond in first person as Jasper.

Core Rules:
- First Person: Always use "I/my/me" (e.g., "I have 2 years of experience with Python")
- Missing Information: If you lack information, say "I don't have that information right now, but you can email me at jasper66018@gmail.com to discuss further"
- Project URLs: When mentioning any project, ALWAYS include its live_url from metadata if it exists
- Source-Based: Only share information from the retrieved context. Don't fabricate details

About Me:
- 2 years as Software Engineer at digiLab (Sept 2023 - June 2025)
- MSc Physics, University of Exeter (2019-2023, 2:1)
- Currently bikepacking England to Bangladesh, building projects
- Contact: jasper66018@gmail.com, WhatsApp +447423781157
- GitHub: github.com/jacantwell, LinkedIn: linkedin.com/in/jasper-cantwell-gill

Technical Strengths: Python (FastAPI, PyTorch), TypeScript (React, Next.js), AWS (Lambda, ECS, S3, CloudFormation), Docker, CI/CD, Microservices, MongoDB, Machine Learning

Tone: Professional but personable, confident, enthusiastic about technology."""


def extract_project_urls_from_context(source_documents):
    """Extract live_url values from source document metadata"""
    urls = {}
    for doc in source_documents:
        metadata = doc.metadata
        
        # Get project name and live_url
        project_name = metadata.get('name') or metadata.get('file_name', '').replace('.md', '')
        live_url = metadata.get('live_url')
        
        # Store if live_url exists and is not null/empty
        if live_url and live_url.lower() != 'null' and live_url.strip():
            urls[project_name] = live_url
    
    return urls


def create_enhanced_context(source_documents):
    """
    Create enhanced context that includes project URLs prominently
    """
    # Extract URLs first
    project_urls = extract_project_urls_from_context(source_documents)
    
    # Build context with URLs highlighted
    context_parts = []
    
    # Add URL information at the top if any exist
    if project_urls:
        context_parts.append("AVAILABLE PROJECT URLS (include these when mentioning these projects):")
        for project, url in project_urls.items():
            context_parts.append(f"- {project}: {url}")
        context_parts.append("\nCONTEXT FROM DOCUMENTS:")
    
    # Add document contents
    for i, doc in enumerate(source_documents, 1):
        file_name = doc.metadata.get('file_name', 'Unknown')
        doc_type = doc.metadata.get('type', 'unknown')
        context_parts.append(f"\n[Source {i}: {file_name} ({doc_type})]")
        context_parts.append(doc.page_content)
    
    return "\n".join(context_parts)


def create_portfolio_chain(vectorstore):
    """Create a QA chain with the system prompt"""
    
    # Custom prompt template that includes system prompt
    prompt_template = f"""{SYSTEM_PROMPT}

Based on the following context, answer the question. Remember to:
1. Respond in first person as Jasper
2. Include live URLs when mentioning projects that have them
3. If you don't have enough information, mention the email contact

Context:
{{context}}

Question: {{question}}

Answer (as Jasper, in first person):"""
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    
    # Use Gemini with appropriate settings
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,  # Slightly creative but still grounded
        max_output_tokens=1024
    )
    
    # Create retrieval chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_kwargs={
                "k": 5  # Retrieve top 5 most relevant chunks
            }
        ),
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )
    
    return qa_chain


def query_portfolio(question: str, vectorstore):
    """
    Query the portfolio with proper context enhancement
    """
    # Create the chain
    qa_chain = create_portfolio_chain(vectorstore)
    
    # Get initial result
    result = qa_chain.invoke({"query": question})
    
    # Extract project URLs from sources
    project_urls = extract_project_urls_from_context(result['source_documents'])
    
    # Check if any URLs were missed in the response
    missed_urls = []
    answer = result['result']
    for project, url in project_urls.items():
        # Check if project is mentioned but URL is not
        if project.lower() in answer.lower() and url not in answer:
            missed_urls.append(f"{project}: {url}")
    
    # If URLs were missed, add them
    if missed_urls:
        answer += "\n\nProject links:\n" + "\n".join(f"- {item}" for item in missed_urls)
        result['result'] = answer
    
    return result


def chat_interface():
    """Interactive chat interface for testing"""
    print("="*60)
    print("JASPER'S PORTFOLIO ASSISTANT")
    print("="*60)
    print("\nLoading vector store...")
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = Chroma(
        persist_directory="./chroma/chroma_db",
        embedding_function=embeddings
    )
    
    print("Ready! Ask me anything about my experience, projects, or skills.")
    print("Type 'quit' to exit.\n")
    
    while True:
        question = input("\nYou: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\nThanks for chatting! Feel free to email jasper66018@gmail.com")
            break
        
        if not question:
            continue
        
        print("\nJasper: ", end="")
        
        try:
            result = query_portfolio(question, vectorstore)
            print(result['result'])
            
            # Optionally show sources
            print("\n[Sources used:", end=" ")
            sources = list(set([doc.metadata.get('file_name', 'unknown') 
                               for doc in result['source_documents']]))
            print(", ".join(sources) + "]")
            
        except Exception as e:
            print(f"Sorry, I encountered an error: {e}")
            print("Feel free to email me directly at jasper66018@gmail.com")


# Example usage in API endpoint (FastAPI)
def create_api_example():
    """Example of how to use this in a FastAPI endpoint"""
    
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    
    app = FastAPI()
    
    # Load vectorstore once at startup
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectorstore = Chroma(
        persist_directory="./chroma/chroma_db",
        embedding_function=embeddings
    )
    
    class Question(BaseModel):
        question: str
    
    class Answer(BaseModel):
        answer: str
        sources: list[str]
    
    @app.post("/ask", response_model=Answer)
    async def ask_question(q: Question):
        """Ask a question about Jasper's portfolio"""
        try:
            result = query_portfolio(q.question, vectorstore)
            
            sources = [doc.metadata.get('file_name', 'unknown') 
                      for doc in result['source_documents']]
            
            return Answer(
                answer=result['result'],
                sources=list(set(sources))
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    return app


if __name__ == "__main__":
    # Run interactive chat
    chat_interface()
