from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.agents import create_agent
from pydantic import BaseModel
from typing import AsyncIterator, Dict, Any, Literal
import logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan event handler for startup and shutdown.
    Initializes vector store and agent on startup.
    """
    print("Starting up the FastAPI application...")
    
    # Initialize embeddings and vector store
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
        app.state.vectorstore = Chroma(
            persist_directory="./chroma/chroma_db", 
            embedding_function=embeddings
        )
        app.state.retriever = app.state.vectorstore.as_retriever(
            search_type="similarity", 
            search_kwargs={"k": 4}
        )
        print("Vector store initialized successfully")
        
        # Define tools (closure over app.state.vectorstore)
        def search_portfolio(query: str) -> str:
            """Search through Jasper's portfolio documents including CV, projects, and experience.
            Use this tool when the user asks about Jasper's background, skills, projects, or experience.
            """
            results = app.state.vectorstore.similarity_search(query, k=3)
            context = "\n\n".join([doc.page_content for doc in results])
            return context
        
        tools = [search_portfolio]
        
        prompt = "You are Jasper's AI assistant. Use the following tools to help answer user questions about Jasper's portfolio, skills, projects, and experience. Use the search_portfolio tool to find relevant information from Jasper's documents when needed and use it to generate complete answers to questions."
        
        # Initialize the Gemini model
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)
        
        # Create the agent
        app.state.agent = create_agent(
            model=model,
            tools=tools,
            system_prompt=prompt,
        )
        print("Agent initialized successfully")
        
    except Exception as e:
        logger.error(f"Failed to initialize vector store or agent: {e}", exc_info=True)
        raise
    
    yield  # Application runs here
    
    # Shutdown
    print("Shutting down the FastAPI application...")
    # Add cleanup if needed (e.g., closing connections)
    if hasattr(app.state, 'vectorstore'):
        delattr(app.state, 'vectorstore')
    if hasattr(app.state, 'retriever'):
        delattr(app.state, 'retriever')
    if hasattr(app.state, 'agent'):
        delattr(app.state, 'agent')


app = FastAPI(lifespan=lifespan)


class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7


async def generate_agent_stream(
    agent: Any,
    user_input: str,
) -> AsyncIterator[Dict[Literal["event", "data"], str]]:
    """
    Streams the agent's response with granular event handling.

    Yields dictionaries containing:
        - 'event': Event type ('update', 'tool', 'error')
        - 'data': The content to stream

    Args:
        agent: The LangChain agent instance
        user_input: The user's input message

    Yields:
        Dict with 'event' and 'data' keys for streaming updates
    """
    logger.info(f"Starting stream for input: '{user_input[:50]}...'")
    
    # Track the last seen text to calculate deltas
    last_text = ""

    try:
        async for chunk in agent.astream(
            {"messages": [{"role": "user", "content": user_input}]},
        ):
            # Skip chunks without model data
            if not chunk.get("model"):
                continue

            messages = chunk["model"].get("messages", [])
            if not messages:
                continue

            last_message = messages[-1]
            content_blocks = getattr(last_message, "content_blocks", [])

            # Skip if no content blocks
            if not content_blocks:
                continue

            last_content_block = content_blocks[-1]
            content_type = last_content_block.get("type")

            if content_type == "text":
                text_content = last_content_block.get("text", "")
                
                # Calculate the delta (new text since last chunk)
                if text_content and text_content != last_text:
                    delta = text_content[len(last_text):]
                    last_text = text_content
                    
                    if delta:
                        yield {"event": "update", "data": delta}

            elif content_type == "tool_call":
                tool_name = last_content_block.get("name", "unknown")
                yield {"event": "tool", "data": f"\n[Using tool: {tool_name}]\n"}
                # Reset text tracking when switching to tool calls
                last_text = ""

    except Exception as e:
        logger.error(f"Error during streaming: {e}", exc_info=True)
        yield {"event": "error", "data": f"Stream error: {str(e)}"}

@app.post("/chat/stream")
async def chat_stream(request: ChatRequest, app_request: Request):
    """
    Streaming chat endpoint.
    Shows all steps including tool calls and final response.
    """
    if not hasattr(app_request.app.state, 'agent'):
        return {"error": "Agent not initialized. Server may still be starting up."}
    
    return EventSourceResponse(
        generate_agent_stream(app_request.app.state.agent, request.message),
    )


@app.get("/health")
async def health_check(request: Request):
    """Health check endpoint"""
    return {
        "status": "healthy",
        "vector_store_ready": hasattr(request.app.state, 'vectorstore'),
        "agent_ready": hasattr(request.app.state, 'agent')
    }


@app.get("/tools")
async def list_tools(request: Request):
    """List available tools"""
    if not hasattr(request.app.state, 'agent'):
        return {"error": "Agent not initialized"}
    
    return {
        "tools": [
            {
                "name": "search_portfolio",
                "description": "Search through Jasper's portfolio documents including CV, projects, and experience."
            }
        ]
    }