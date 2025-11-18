from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.agents import create_agent
from langchain_pinecone import PineconeVectorStore
import os
from pydantic import BaseModel
from typing import AsyncIterator, Dict, Any, Literal
import logging
import re

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

        # Initialize embeddings model (must be the SAME model used during upsert)
        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001",
        )

        # Initialize LangChain Pinecone vector store
        app.state.vectorstore = PineconeVectorStore(
            index_name="portfolio",
            embedding=embeddings,
            pinecone_api_key=os.getenv("PINECONE_API_KEY"),
        )
        print("Vector store initialized successfully")

        # Define tools (closure over app.state.vectorstore)
        def search_portfolio(query: str) -> str:
            """Search through Jasper's portfolio documents including CV, projects, and experience.
            Use this tool when the user asks about Jasper's background, skills, projects, or experience.
            """
            results = app.state.vectorstore.similarity_search(query, k=5)

            # Extract project URLs from metadata
            project_urls = {}
            for doc in results:
                metadata = doc.metadata
                project_name = metadata.get("name") or metadata.get(
                    "file_name", ""
                ).replace(".md", "")
                live_url = metadata.get("live_url")

                # Store if live_url exists and is not null/empty
                if live_url and live_url.lower() != "null" and live_url.strip():
                    project_urls[project_name] = live_url

            # Build context with URLs prominently featured
            context_parts = []

            # Add URL information at the top if any exist
            if project_urls:
                context_parts.append(
                    "IMPORTANT - Project URLs (ALWAYS include these when mentioning these projects):"
                )
                for project, url in project_urls.items():
                    context_parts.append(f"  • {project}: {url}")
                context_parts.append("\nContext from documents:")

            # Add document contents
            for doc in results:
                context_parts.append(f"\n---\n{doc.page_content}")

            return "\n".join(context_parts)

        tools = [search_portfolio]

        SYSTEM_PROMPT = """You are an AI assistant representing Jasper Cantwell, a full-stack software engineer. You respond in first person as Jasper.

        Core Rules:
        1. First Person: ALWAYS use "I/my/me" (e.g., "I have 2 years of experience with Python"). NEVER use "Jasper" or "he/his".
        
        2. Project URLs: CRITICAL - When mentioning any project, ALWAYS include its URL if provided in the tool results. 
           Example: "I built findkairos.com, which you can check out at https://findkairos.com"
           The tool results will show URLs at the top - make sure to include them naturally in your response.
        
        3. Missing Information: If you lack information after using the search tool, say: 
           "I don't have that information available right now, but feel free to email me at jasper66018@gmail.com to discuss further."
        
        4. Source-Based: Only share information from the tool results. Don't fabricate details.
        
        5. Use the search_portfolio tool for ANY question about my background, experience, skills, or projects.

        6. For any requests that are not relevant to Jasper or his project respond with "Sorry this is not relevant, please try asking something else."

        About Me (use when relevant):
        - 2 years as Software Engineer at digiLab (Sept 2023 - June 2025)
        - MSc Physics, University of Exeter (2019-2023, 2:1)
        - Currently bikepacking England to Bangladesh, building projects along the way
        - Contact: jasper66018@gmail.com | WhatsApp: +447423781157
        - GitHub: github.com/jacantwell | LinkedIn: linkedin.com/in/jasper-cantwell-gill

        Key Technical Strengths (highlight when relevant):
        Python (FastAPI, PyTorch, BoTorch), TypeScript (React, Next.js), AWS (Lambda, ECS, S3, CloudFormation, Cognito, CloudWatch), Docker, CI/CD, Microservices, Event-Driven Architecture, MongoDB, Machine Learning

        Response Strategy:
        1. Use the search tool to find relevant information
        2. Respond in first person with specific examples
        3. Include project URLs naturally when mentioning projects
        4. Be professional but personable - confident and enthusiastic about technology
        5. Keep responses focused and concise (aim for 150-300 words unless more detail is needed)
        6. Format responses using markdown where it seems suitable.
        7. Use markdown formatting to highlight key technical terms

        Example responses:
        Q: "What projects have you built?"
        A: "I've built several full-stack projects. findkairos.com (https://findkairos.com) is a web app connecting bikepackers worldwide, using Python FastAPI with MongoDB and Next.js. I also built jaspercycles.com (https://jaspercycles.com) which tracks my bikepacking journey in real-time using the Strava API. Both demonstrate my ability to design, build, and deploy production applications independently."
        
        Q: "What experience do you have with Python?"
        A: "I have 2 years of professional Python experience from digiLab, primarily with FastAPI for building production APIs. I also used PyTorch and BoTorch to extend our ML library with Gaussian Process models. You can see my Python work in action at findkairos.com (https://findkairos.com), which uses FastAPI with MongoDB for the backend."
        """

        # Initialize the Gemini model
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)

        # Create the agent
        app.state.agent = create_agent(
            model=model,
            tools=tools,
            system_prompt=SYSTEM_PROMPT,
        )
        print("Agent initialized successfully")

    except Exception as e:
        logger.error(f"Failed to initialize vector store or agent: {e}", exc_info=True)
        raise

    yield  # Application runs here

    # Shutdown
    print("Shutting down the FastAPI application...")
    # Add cleanup if needed (e.g., closing connections)
    if hasattr(app.state, "vectorstore"):
        delattr(app.state, "vectorstore")
    if hasattr(app.state, "retriever"):
        delattr(app.state, "retriever")
    if hasattr(app.state, "agent"):
        delattr(app.state, "agent")


app = FastAPI(lifespan=lifespan)

# Configure CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"
    ],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageDict(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[MessageDict]
    temperature: float = 0.7


def extract_project_urls_from_context(context: str) -> Dict[str, str]:
    """
    Extract project URLs from the tool context.
    Returns a dict of {project_name: url}
    """
    urls = {}
    # Look for the IMPORTANT section that lists URLs
    url_pattern = r"  • (.+?): (https?://[^\s]+)"
    matches = re.findall(url_pattern, context)
    for project_name, url in matches:
        urls[project_name.strip()] = url.strip()
    return urls


def ensure_urls_in_response(response: str, project_urls: Dict[str, str]) -> str:
    """
    Verify that project URLs are included when projects are mentioned.
    If a project is mentioned without its URL, append it naturally.

    Args:
        response: The agent's response text
        project_urls: Dict of {project_name: url} from context

    Returns:
        Response with URLs added if they were missing
    """
    if not project_urls:
        return response

    missing_urls = []
    response_lower = response.lower()

    for project, url in project_urls.items():
        project_lower = project.lower()
        # Check if project is mentioned but URL is not
        if project_lower in response_lower and url not in response:
            # Check common variations
            project_variations = [
                project_lower,
                project_lower.replace("_", ""),
                project_lower.replace("-", ""),
                project_lower.replace(".md", ""),
            ]

            mentioned = any(var in response_lower for var in project_variations)
            if mentioned:
                missing_urls.append(f"{project}: {url}")

    # If URLs were missed, append them
    if missing_urls:
        response += "\n\n**Project Links:**\n" + "\n".join(
            f"- {item}" for item in missing_urls
        )

    return response


async def generate_agent_stream(
    agent: Any,
    messages: list[MessageDict],
) -> AsyncIterator[Dict[Literal["event", "data"], str]]:
    """
    Streams the agent's response with granular event handling.

    Ensures project URLs are included when projects are mentioned.

    Yields dictionaries containing:
        - 'event': Event type ('update', 'tool', 'error')
        - 'data': The content to stream

    Args:
        agent: The LangChain agent instance
        messages: The full conversation history (list of message dicts with role and content)

    Yields:
        Dict with 'event' and 'data' keys for streaming updates
    """
    # Get the last user message for logging
    last_user_msg = next((msg.content for msg in reversed(messages) if msg.role == "user"), "")
    logger.info(f"Starting stream for input: '{last_user_msg[:50]}...' (with {len(messages)} messages in history)")

    # Track the last seen text to calculate deltas
    last_text = ""
    tool_context = ""  # Track context from tool calls
    project_urls = {}  # Track project URLs from context

    # Convert MessageDict objects to dicts for the agent
    messages_list = [{"role": msg.role, "content": msg.content} for msg in messages]

    try:
        async for chunk in agent.astream(
            {"messages": messages_list},
        ):
            # Skip chunks without model data
            if not chunk.get("model"):
                # Check for tool results in other parts of the chunk
                if "tool" in chunk:
                    tool_data = chunk.get("tool", {})
                    if "result" in tool_data:
                        tool_context = tool_data["result"]
                        # Extract URLs from tool context
                        project_urls = extract_project_urls_from_context(tool_context)
                        logger.info(f"Extracted project URLs: {project_urls}")
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
                    delta = text_content[len(last_text) :]
                    last_text = text_content

                    if delta:
                        yield {"event": "update", "data": delta}

            elif content_type == "tool_call":
                # Track tool calls to capture context
                tool_name = last_content_block.get("name", "unknown")
                logger.info(f"Tool called: {tool_name}")
                # Optionally notify user
                # yield {"event": "tool", "data": f"\n[Searching portfolio...]\n"}

        # After streaming is complete, verify URLs were included
        if project_urls and last_text:
            verified_text = ensure_urls_in_response(last_text, project_urls)
            if verified_text != last_text:
                # URLs were missing, append them
                additional_text = verified_text[len(last_text) :]
                logger.info(f"Adding missing URLs: {additional_text[:100]}")
                yield {"event": "update", "data": additional_text}

    except Exception as e:
        logger.error(f"Error during streaming: {e}", exc_info=True)
        yield {"event": "error", "data": f"Stream error: {str(e)}"}


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest, app_request: Request):
    """
    Streaming chat endpoint.
    Shows all steps including tool calls and final response.
    Accepts full conversation history for context-aware responses.
    """

    print("Not input validation")

    if not hasattr(app_request.app.state, "agent"):
        return {"error": "Agent not initialized. Server may still be starting up."}

    return EventSourceResponse(
        generate_agent_stream(app_request.app.state.agent, request.messages),
    )


@app.get("/health")
async def health_check(request: Request):
    """Health check endpoint"""
    return {
        "status": "healthy",
        "vector_store_ready": hasattr(request.app.state, "vectorstore"),
        "agent_ready": hasattr(request.app.state, "agent"),
    }


@app.get("/tools")
async def list_tools(request: Request):
    """List available tools"""
    if not hasattr(request.app.state, "agent"):
        return {"error": "Agent not initialized"}

    return {
        "tools": [
            {
                "name": "search_portfolio",
                "description": "Search through Jasper's portfolio documents including CV, projects, and experience.",
            }
        ]
    }


@app.get("/debug/search")
async def debug_search(request: Request, query: str = "projects"):
    """
    Debug endpoint to test the search tool and URL extraction.
    Example: /debug/search?query=projects
    """
    if not hasattr(request.app.state, "vectorstore"):
        return {"error": "Vector store not initialized"}

    # Test the search
    results = request.app.state.vectorstore.similarity_search(query, k=5)

    # Extract URLs
    project_urls = {}
    for doc in results:
        metadata = doc.metadata
        project_name = metadata.get("name") or metadata.get("file_name", "").replace(
            ".md", ""
        )
        live_url = metadata.get("live_url")

        if live_url and live_url.lower() != "null" and live_url.strip():
            project_urls[project_name] = live_url

    return {
        "query": query,
        "num_results": len(results),
        "project_urls_found": project_urls,
        "sample_metadata": [
            {
                "file": doc.metadata.get("file_name", "unknown"),
                "type": doc.metadata.get("type", "unknown"),
                "has_live_url": "live_url" in doc.metadata,
                "live_url": doc.metadata.get("live_url", None),
            }
            for doc in results[:3]
        ],
    }
