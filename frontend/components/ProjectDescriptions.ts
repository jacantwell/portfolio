export const jaspercyclesDescription = `

## Overview
This repo contains the code for my personal website jaspercycles.com. This uses the public Strava API to track my bikepacking journey around the globe, plotting my cycles on a MapBox map. The map is interactive and you can click sections of the journey to load my details and photos. The wesbiste alos functions functions as blog with blog posts appearing below the map.

## Technical Implementation
### Frontend
 - Language: TypeScript/JavaScript
 - Framework: React/Vite/TailwindCSS
 - Key featurs: [MapBox, RestAPI, Blog]

### Infrastructure
 - Cloud Provider: AWS
 - Services: S3, Cloudfront, Route53
 - Deployment: [Github Action]

## Key Achievments
 - Comprhensive CI/CD pipe deploying both the static page and blog posts.
 - Markdown processing of blog posts.
 - Dark mode
 - Browser caching 

`;

export const kairosDescription = `

Kairos is a bikepacking journey tracking application. The platform allows users to create journeys, add markers (both past and planned), and discover other bikepackers near their routes.

## Technical Implementation
### Frontend
- Language: TypeScript/JavaScript
- Framework: React/Next.js/TailwindCSS
- Key features: [OAuthFlow, Email Verification, NextJS App Router]

### Backend
- **Framework:** FastAPI 0.115.13
- **Language:** Python 3.12+
- **Database:** MongoDB (Atlas)
- **Authentication:** JWT (PyJWT)
- **Password Hashing:** Bcrypt + Passlib
- **Email Service:** Resend
- **Deployment:** AWS Lambda (via Mangum)
- **Infrastructure:** AWS CloudFormation
- **Container:** Docker (ECR)
- **Dependency Management:** Poetry

### Infrastructure
- Cloud Provider: AWS
- Services: Cloudfront, Router 53, Cloudfront S3
- Deployment: [Github Action]

## Key Achievements
 - Implements OAuth flow with email verification.
 - User session management allowing users to remain logged in.
 - NextJS App Router for page naviagtion.
 - Tanstack integration for API queries.
 - Re-usable componets allowing for easy development.
`;


export const s3mobileDescription = `


While travelling, my camera roll filled up so quickly that I found myself in a bind: I didn't want to get stuck paying for an ongoing, expensive cloud subscription service, but I also didn't have easy access to a hard drive for offloading photos. My personal solution to this problem is this app. I designed the S3 Mobile App not as a cloud storage alternative, but as a cheap, easy-to-use, temporary storage solution. It lets me quickly dump media from my phone into my own AWS S3 bucket to free up space until I get home. To use this project yourself (on your Android phone), all you'll need is an AWS and Expo account.

## Technical Implementation

### Frontend
- Language: TypeScript
- Framework: React Native 0.81.4, React 19, Expo SDK 54
- Navigation: Expo Router 6 with file-based routing
- State Management: React Native Async Storage
- AWS Integration: AWS SDK v3 (Cognito Identity, Lambda Client)
- Image Handling: Expo Image Picker with camera and gallery support
- Key Features: Direct S3 uploads via pre-signed URLs, unauthenticated Cognito identity provider, native Android permissions handling

### Backend
- Language: Python 3.12
- Compute: AWS Lambda (serverless)
- Storage: Amazon S3 with intelligent lifecycle policies
- Authentication: AWS Cognito Identity Pool (unauthenticated access)
- Key Features: Pre-signed URL generation, timestamp-based file naming, automatic CORS handling

### Infrastructure
- Infrastructure as Code: AWS CloudFormation
- Cloud Provider: AWS (S3, Lambda, Cognito, IAM)
- Deployment Strategy: Automated CloudFormation stack deployment
- Mobile Deployment: Expo Application Services (EAS) for Android builds
- CI/CD: Automated build pipeline with environment secret management

## Key Achievements

- **Serverless Architecture**: Designed and implemented a fully serverless mobile upload system using AWS Lambda and S3, eliminating server maintenance costs and achieving near-infinite scalability with pay-per-use pricing.

- **Infrastructure as Code**: Built a complete CloudFormation template that provisions all AWS resources (S3 buckets, Lambda functions, Cognito Identity Pools, IAM roles) with a single command, enabling reproducible deployments and version-controlled infrastructure.

- **Cost-Optimized Storage Strategy**: Implemented intelligent S3 lifecycle policies that automatically transition photos to Deep Archive after 5 days and delete after 1 year, reducing storage costs by up to 95% compared to standard S3 pricing.

- **Secure Pre-Signed URL Pattern**: Developed a secure upload mechanism using Lambda-generated pre-signed URLs with configurable expiration times, allowing direct client-to-S3 uploads without exposing AWS credentials in the mobile app.

- **Modern React Native Development**: Leveraged the latest React 19 and Expo SDK 54 with Expo Router for file-based routing, providing a maintainable codebase with type-safe navigation and automatic code splitting.

- **Unauthenticated Identity Architecture**: Implemented AWS Cognito Identity Pool with unauthenticated access, providing temporary AWS credentials to mobile clients without requiring user authentication, perfect for personal use cases.

- **Automated Deployment Pipeline**: Created comprehensive setup scripts that automate the entire deployment process from AWS infrastructure provisioning to EAS configuration and secret management, reducing setup time from hours to minutes.

- **Cross-Platform Compatibility**: Built with React Native and Expo for easy deployment to both Android and iOS platforms, with comprehensive permission handling for camera and photo library access.

## Architecture Highlights

### Image Upload Pipeline
1. User selects images from gallery or camera using Expo Image Picker
2. React Native app authenticates with AWS Cognito Identity Pool (unauthenticated)
3. App invokes Lambda function via AWS SDK with filename and metadata
4. Lambda function generates pre-signed S3 PUT URL with 1-hour expiration
5. App performs direct HTTP PUT to S3 using pre-signed URL
6. S3 stores image with timestamp-prefixed key to prevent overwrites
7. After 5 days, S3 lifecycle policy automatically transitions to Deep Archive
8. After 1 year, images are automatically deleted to minimize costs

### Infrastructure Deployment Pipeline
1. Developer runs automated setup script with configuration parameters
2. Lambda deployment package is zipped and uploaded to staging S3 bucket
3. CloudFormation stack creates all resources with proper IAM permissions
4. Stack outputs (Identity Pool ID, Lambda name, bucket name) are extracted
5. Environment variables are injected into frontend .env file
6. EAS project is configured with Expo username and secrets
7. Secrets are pushed to EAS for secure cloud builds
8. Developer can build APK via EAS or run locally with Expo Go

### Security Features
- **No Credentials in Code**: AWS credentials never stored in mobile app; Cognito provides temporary credentials
- **Least Privilege IAM**: Cognito role only has permission to invoke specific Lambda function
- **Pre-Signed URL Expiration**: Upload URLs expire after 1 hour to prevent unauthorized access
- **Public Access Blocking**: S3 bucket configured to block all public access by default
- **CORS Configuration**: Restricted CORS policy allowing only PUT/POST from specific origins
- **Environment Secret Management**: Sensitive configuration stored in EAS secrets, never committed to git
`;

export const gitlogDescription = `

# Git-Log

I've always been terrible at keeping track of my accomplishments at work. Everyone says you should maintain a log of what you've done for when you need to update your CV or go for a promotion, but I never actually do it. Then I realized that 99% of my work is already tracked on GitHub through my commits and pull requests. So why not just use that data?

This project pulls your GitHub commit and PR history using the GitHub REST API and uses LLMs to turn it into a readable summary of everything you've worked on. It's basically an automated way to document your accomplishments without having to remember to write them down. Plus, knowing that this tool exists has actually inspired me to write better commit messages and create higher quality PRs, since garbage in means garbage out.

## Technical Implementation

### Backend
- Language: Go 1.24
- Core Libraries: Google Generative AI SDK, standard library HTTP client
- AI Model: Google Gemini (gemini-2.5-flash via AI Studio)
- Key Features: GitHub REST API integration, intelligent work log synthesis, automated report generation

### Infrastructure
- Version Control: Git
- API Integration: GitHub REST API v3
- AI Provider: Google AI Studio
- Deployment: Shell script automation, environment-based configuration

## Key Achievements

- **GitHub API Integration**: Implemented a robust GitHub REST API client that efficiently queries commit and pull request history using the Search API with proper pagination, query parameter encoding, and error handling.

- **Intelligent Data Processing**: Built a sophisticated data grouping and filtering system that organizes commits and PRs by repository, extracts essential metadata, and maintains chronological ordering for optimal analysis.

- **AI-Powered Report Synthesis**: Leveraged Google Gemini AI with custom system prompts to transform raw Git data into professional accomplishment reports, intelligently merging new work with existing documentation.

- **Living Document Architecture**: Designed an incremental update system that analyzes existing reports and seamlessly merges new activity, preventing duplication and maintaining a coherent narrative across multiple report generations.

- **Work-in-Progress Detection**: Implemented smart logic to identify incomplete work based on commit patterns and PR metadata, automatically categorizing items into a dedicated WIP section until they're ready for main documentation.

- **Type-Safe Data Models**: Created comprehensive Go structs modeling GitHub's API responses, ensuring type safety and enabling efficient data transformation throughout the processing pipeline.

- **Configurable Time Windows**: Built flexible configuration system supporting custom lookback periods, allowing users to generate reports for any timeframe (default 30 days).

- **Professional Output Format**: Generates well-structured Markdown reports organized by repository and feature workstreams, with automatic feature title generation and impact-focused descriptions.

## Architecture Highlights

### Data Collection Pipeline
1. Load configuration from environment variables (GitHub token, username, date range)
2. Query GitHub Search API for commits and pull requests within specified timeframe
3. Parse JSON responses into strongly-typed Go structs
4. Filter and transform data to extract essential information (PR titles, commit messages, dates, URLs)
5. Group activity by repository with alphabetical sorting
6. Generate summary statistics (total repos, PRs, commits, date range)

### AI Report Generation Pipeline
1. Load system prompt containing synthesis instructions and formatting guidelines
2. Read existing accomplishment report (if present) to enable incremental updates
3. Marshal work log data to JSON for AI processing
4. Construct user prompt combining existing report and new Git activity data
5. Send request to Google Gemini AI with system instructions for intelligent merging
6. AI analyzes patterns, identifies related work, generates feature titles
7. AI synthesizes new entries or updates existing ones, maintaining narrative coherence
8. Write generated report to disk in Markdown format

### Intelligent Synthesis Features
- **Duplicate Detection**: AI scans existing report for PR numbers and feature descriptions to prevent redundant entries
- **Work Continuation**: Identifies ongoing features across multiple PRs and updates existing sections rather than creating duplicates
- **Feature Grouping**: Clusters related PRs under meaningful feature titles (e.g., "User Authentication API", "Performance Optimization")
- **Impact Translation**: Converts technical commit messages into business-value descriptions
- **WIP Management**: Automatically promotes work from WIP section to main report when sufficient progress is detected
`;

export const portfolioDescription =`

An intelligent, conversational portfolio website featuring an AI chatbot that can answer questions about my experience, projects, and technical skills in real-time. The application leverages modern web technologies with a production-ready RAG (Retrieval Augmented Generation) implementation.

## Technical Implementation

### Frontend
- Language: TypeScript
- Framework: Next.js 16 (App Router), React 19
- Styling: Tailwind CSS 4
- UI Components: Custom Retro UI library built on Radix UI primitives
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
`