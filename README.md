# AI-Powered Portfolio

An intelligent, conversational portfolio website featuring an AI chatbot that can answer questions about my experience, projects, and technical skills in real-time. The application leverages modern web technologies with a production-ready RAG (Retrieval Augmented Generation) implementation.

## Technical Implementation

### Frontend
- Language: TypeScript
- Framework: Next.js 16 (App Router), React 19
- Styling: Tailwind CSS 4
- UI Components: Retro UI library built on Radix UI primitives
- Key Features: Server-Sent Events (SSE) streaming, React Markdown rendering, typewriter effect for chat messages

### Backend
- Language: Python
- Framework: FastAPI
- AI/ML Stack: LangChain, Google Gemini AI (gemini-2.5-flash-lite, gemini-embedding-001)
- Vector Database: Pinecone (Serverless, AWS us-east-1)
- Key Features: RAG implementation, custom document processing pipeline, SSE streaming endpoints

### Infrastructure
- Cloud Provider: Vercel (Frontend & Backend)
- Vector Database: Pinecone on AWS
- CI/CD: Vercel Git Integration
- Deployment: Automatic deployment on push to main branch

## Key Achievements

- **Production RAG System**: Implements a complete Retrieval Augmented Generation pipeline using Pinecone vector database for semantic search across portfolio documents, CV, and project READMEs.

- **Real-Time Streaming Chat**: Built a custom SSE (Server-Sent Events) streaming implementation for real-time AI responses with typewriter effect, providing a smooth conversational experience.

- **Intelligent Document Processing**: Developed a sophisticated document chunking pipeline that adapts chunk size and overlap based on document type (profile, project, application) for optimal retrieval quality.

- **LangChain Agent Architecture**: Implemented a custom LangChain agent with tools for semantic search, automatic project URL extraction, and context-aware responses.

- **Custom UI Component Library**: Created a reusable "Retro UI" component library on top of Radix UI, ensuring accessibility and consistent design patterns throughout the application.

- **Modern Full-Stack Architecture**: Leveraged the latest versions of Next.js 16 and React 19 with the App Router pattern for optimal performance and developer experience.

- **YAML Frontmatter Support**: Built a metadata extraction system that processes YAML frontmatter from markdown files, enabling rich metadata tagging and improved search relevance.

- **Type-Safe Development**: Fully typed TypeScript frontend with strict type checking, improving code quality and maintainability.

## Architecture Highlights

### AI Chat Pipeline
1. User submits query through the frontend interface
2. Frontend establishes SSE connection to FastAPI backend
3. LangChain agent uses custom search tool to query Pinecone vector database
4. Relevant document chunks are retrieved using semantic similarity
5. Google Gemini AI generates contextual response based on retrieved information
6. Response is streamed back to frontend in real-time using SSE
7. Frontend displays response with typewriter effect for natural conversation flow

### Document Ingestion Pipeline
1. Markdown and PDF files with YAML frontmatter metadata
2. Custom text splitter with document-type-specific chunking strategies
3. Google Gemini embeddings (gemini-embedding-001, 3072 dimensions)
4. Batch upsert to Pinecone with metadata preservation
5. Automatic URL extraction and tracking for project references

## Development Setup

### Prerequisites
- Node.js 20+
- Python 3.11+
- Pinecone API key
- Google AI API key

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### Backend Setup
```bash
cd backend
uv sync
uv run uvicorn app:app --reload
```

### Environment Variables
Create `.env` file in the backend directory:
```
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## Project Structure
```
portfolio/
├── frontend/          # Next.js frontend application
│   ├── app/          # Next.js App Router pages
│   ├── components/   # React components
│   │   ├── retroui/  # Custom UI component library
│   │   ├── ChatInterface.tsx
│   │   └── Sidebar.tsx
│   └── lib/          # Utility functions
├── backend/          # FastAPI backend application
│   ├── app.py       # Main FastAPI application with LangChain agent
│   ├── scripts/     # Utility scripts
│   │   └── build_pinecone.py  # Document processing & vector DB setup
│   └── pyproject.toml
└── README.md
```
