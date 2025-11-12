from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.agents import create_agent
import asyncio


# Initialize embeddings and vector store (do this once at startup)
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
vectorstore = Chroma(
    persist_directory="./chroma/chroma_db",
    embedding_function=embeddings
)
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

# Define some example tools for the agent
def get_current_time() -> str:
    """Get the current time in a human-readable format."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """
    Calculate a mathematical expression.
    Args:
        expression: A mathematical expression to evaluate (e.g., "2 + 2", "10 * 5")
    """
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error calculating: {str(e)}"


def search_info(query: str) -> str:
    """
    Search for information (simulated).
    Args:
        query: The search query
    """
    return f"Search results for '{query}': This is a simulated search result. In production, integrate with a real search API."

# Define tools
def search_portfolio(query: str) -> str:
    """Search through Jasper's portfolio documents including CV, projects, and experience.
    Use this tool when the user asks about Jasper's background, skills, projects, or experience."""
    results = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in results])
    return context

# Define available tools
tools = [get_current_time, calculate, search_info, search_portfolio]

prompt ="You are Jasper's AI assistant. Use the following tools to help answer user questions about Jasper's portfolio, skills, projects, and experience., Use the search_portfolio tool to find relevant information from Jasper's documents when needed and use it to generate complete answers to questions."
# prompt ="You are an assistant. When you use a tool, always include the tool's result in your final answer to the user."

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.7
)

# Create the agent
graph = create_agent(
    model=model,
    tools=tools,
    system_prompt=prompt,
)

# --- 7. Define the Async Streaming Function ---
async def stream_agent_response(user_input):
    """
    Streams the agent's response word-by-word for the *final answer*.
    """
    print(f"\n--- 🗣️ Streaming response for: '{user_input}' ---")
    
    # astream_events is the best way to get granular, real-time events
    async for chunk in graph.astream(
        {"messages": [{"role": "user", "content": user_input}]},
        # stream_mode="messages"
    ):

        # We want to output content from model events
        if chunk.get('model'):
            # We find the latest message
            last_message = chunk['model']['messages'][-1]
            # If the event was a tool call there may not be any content so we skip
            if len(last_message.content_blocks) == 0:
                continue
            last_content_block = last_message.content_blocks[-1]
            content_type = last_content_block['type']
            # If the content type is text we print the text
            if content_type == "text":
                print(last_content_block['text'], end="", flush=True)
            # If it is a tool call we can show the user a message saying we are using a tool
            elif content_type == "tool_call":
                print("Using tool:", last_content_block['name'])
        
        
    print("\n--- ✅ End of stream ---")

# --- 8. Main Async Function to Run the Test ---
async def main():
    # Test 1: A simple question (no tool use)
    await stream_agent_response("Hi, how are you today?")
    
    print("\n" + "="*50 + "\n")
    
    # Test 2: A question that *should* use a tool
    try:
        await stream_agent_response("can you tell me what tech stack the git-log project uses")
    except Exception as e:
        raise e

# --- 9. Run the main function ---
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")