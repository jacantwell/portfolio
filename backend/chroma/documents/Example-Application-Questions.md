# Locai Labs Application Responses

## Question 5: Why do you want to work at Locai Labs?

What draws me to Locai Labs is the opportunity to contribute to foundational AI development from within the UK. Having spent the past two years building ML workflow platforms and agentic systems, I've seen firsthand how critical the underlying infrastructure and engineering excellence are to creating truly capable AI systems. Your mission to advance cutting-edge AI through deep technical innovation resonates with my own approach to engineering.

I'm particularly excited about Locai Labs' focus on building world-class LLMs with an emphasis on cost and efficiency alongside capability. At digiLab, I worked on systems where computational efficiency directly impacted our ability to serve clients, so I appreciate the engineering challenges involved in optimizing large-scale AI systems. The chance to work on foundational models, agentic applications, and developer tools that enable intelligent automation aligns perfectly with where I want to take my career.

Your small, highly technical team structure also appeals to me. At digiLab, I was selected for a scout team with the CEO and CTO to design our event-driven microservice architecture, and I thrived in that environment where individual contributions directly shaped the product. The fact that every engineer at Locai Labs helps define architecture and product direction is exactly the kind of ownership and impact I'm looking for.

## Question 6: How many years of professional software engineering experience do you have?

2 years (September 2023 - June 2025 at digiLab)

## Question 7: What excites you about building AI systems and agentic tools?

What excites me most about building AI systems is the intersection of complex engineering challenges and tangible real-world impact. During my time at digiLab, I worked on an ML workflow platform that used LangChain to provide agentic solutions, and I found the orchestration challenges fascinating. There's something uniquely satisfying about designing systems that can reason, plan, and execute tasks autonomously while remaining reliable and maintainable at scale.

The technical depth required is what really draws me in. Building production-ready agentic systems isn't just about integrating an LLM API; it requires thoughtful architecture around state management, error handling, workflow orchestration, and observability. I love problems that span multiple layers of the stack, from designing efficient data pipelines and event-driven architectures to implementing robust authentication and monitoring systems.

I'm also excited by the rapid evolution of the field. The shift from simple prompt-response patterns to sophisticated multi-agent systems with tool use and reasoning capabilities opens up entirely new categories of applications. Having extended our internal ML library with Gaussian Process models for uncertainty quantification, I appreciate how important it is to understand not just what an AI system outputs, but how confident we can be in those outputs. Building systems that are both powerful and trustworthy is a challenge I find deeply motivating.

## Question 8: Describe a backend or AI-related project you've worked on that you're proud of. What was your role and what technologies did you use?

One of my most impactful projects at digiLab was rapidly bringing a complex microservice from concept to production in just 2 months, despite constantly shifting requirements. This service was a core component of our ML workflow platform and needed to handle user authentication, integrate with our event-driven architecture, and provide analytics capabilities.

I was the lead engineer responsible for the entire backend implementation. The technical stack included:
- Python FastAPI for the REST API with Pydantic for robust data validation
- AWS Cognito for token-based authentication and user management
- AWS CloudWatch for user analytics and operational monitoring
- AWS SQS for event-driven communication with other microservices
- Docker containerization deployed on AWS ECS
- CloudFormation for infrastructure as code
- GitHub Actions for CI/CD automation

The challenge was building something production-ready while requirements were evolving based on client feedback. I implemented a modular architecture with clear separation of concerns, which allowed me to adapt quickly without accumulating technical debt. The authentication layer was particularly complex, as it needed to support multiple user types with different permission levels while integrating seamlessly with our existing infrastructure.

What I'm most proud of is that despite the time pressure and shifting requirements, the service launched successfully and has been running reliably in production. The modular design I implemented also made it significantly easier for data scientists on the team to contribute features independently, which accelerated our overall development velocity. This project taught me a lot about balancing speed with quality and the importance of clear API design in distributed systems.

## Question 9: Have you previously completed any AI-related personal or research projects? (If yes, briefly describe.)

**Master's Thesis (2023):** My thesis focused on "The Application of Machine Learning to the Inverse Scattering Problem." I built neural networks using TensorFlow to solve inverse problems in physics, which gave me hands-on experience with the challenges of applying ML to real-world scientific problems where data quality and physical constraints matter.

**Professional ML Work at digiLab:** I extended our internal machine learning library with Gaussian Process models using PyTorch and BoTorch, which improved uncertainty quantification for production ML workflows. This involved implementing Bayesian optimization techniques that helped our clients make better decisions based on model predictions.

**Production Agentic Systems:** For digiLab's newest product, I was responsible for taking our CTO's LangChain prototype code and transforming it into a production-ready, cloud-native platform. This was a core product engineering challenge that involved more than just "making it work" - I had to design robust interfaces, implement comprehensive error handling, and adapt the code for cloud environments where constraints like file loading for RAG pipelines work fundamentally differently than on local machines.

I built the microservice backend that powered our no-code AI platform, using LangChain agents and tools to enable users to build sophisticated workflows without writing code. The technical challenges included making the system safe and reliable for end users - implementing proper error boundaries, adding comprehensive pytest test coverage, and designing APIs that could handle the unpredictable nature of LLM outputs gracefully.

The platform supported real-world use cases including agentic RAG workflows for nuclear engineers, AI triage systems for the healthcare company KOYO, ML model integration where agents could suggest and comment on Gaussian Process model parameters, and customizable message-based chat functions. This work gave me deep practical experience with the challenges of building production agentic systems: managing state across agent interactions, handling tool execution failures, and ensuring the system remained reliable even when LLMs produced unexpected outputs.

## Question 10: Is there anything else you'd like us to know about your background, experience, or interests?

A few additional points that might be relevant:

**Physics Background:** My physics degree has fundamentally shaped how I approach software engineering. The mathematical rigor and analytical problem-solving skills I developed translate directly to system design and debugging complex distributed systems. My thesis on inverse problems using ML gave me a solid foundation in understanding the theoretical underpinnings of machine learning, not just the practical implementation.

**Mentorship and Knowledge Sharing:** I've consistently received positive feedback for being approachable and supportive with team members. At digiLab, I helped onboard graduate hires and delivered technical presentations to help the team level up. I believe strong teams are built on knowledge sharing, and I enjoy helping others grow.

**Advocacy and Leadership:** I served as the employee association representative at digiLab, leading discussions with founders about workplace improvements. This experience taught me how to advocate effectively for team needs while understanding business constraints, and it resulted in tangible improvements like secured office amenities and the formation of an internal AI ethics committee.

**Current Journey:** I'm currently on a bikepacking trip from England toward Bangladesh, and I've been building and deploying software projects along the way. This demonstrates my genuine passion for software development (I literally can't stop coding even while cycling across continents!) and my ability to deliver production-quality work independently with minimal resources.

**Open Source and Community:** My GitHub profile (github.com/jacantwell) showcases my personal projects and coding approach. I believe in building in public and contributing back to the developer community.

## Question 11: Our environment is fast-moving and hands-on. Engineers often take ownership of both infrastructure and backend services. What interests you about working in this kind of environment?

This type of environment is exactly where I thrive. At digiLab, I took full ownership of services from infrastructure provisioning to production deployment, and I genuinely enjoyed the end-to-end responsibility.

What interests me most is the direct connection between decisions and outcomes. When you own both infrastructure and application code, you can make architectural choices that optimize for the specific needs of your system rather than working within rigid constraints. For example, when designing our microservice architecture at digiLab, I could choose the right AWS services (Lambda vs ECS, SQS vs SNS) based on actual usage patterns and cost considerations, then implement the infrastructure as code alongside the application logic. This holistic approach leads to better systems.

I also appreciate the learning opportunities. Managing infrastructure forces you to think about operational concerns like monitoring, logging, scalability, and cost optimization from day one. Deploying my own services taught me to write more maintainable code because I knew I'd be the one debugging it at 2am if something went wrong. That ownership mindset leads to better engineering practices.

The fast-paced aspect is equally appealing. I performed well under pressure when I built our authentication microservice in 2 months with shifting requirements. The key is staying pragmatic: shipping something good quickly is better than pursuing perfection slowly. In a startup environment, you need to balance technical excellence with business needs, and I enjoy that challenge.

Finally, the hands-on nature means you're always learning. At digiLab, I went from basic Docker knowledge to designing entire CloudFormation templates and CI/CD pipelines. When you take ownership of the full stack, every problem becomes an opportunity to deepen your expertise.

## Question 12: Are you currently employed? If not, what was your most recent role and when did it end?

I am not currently employed. My most recent role was Software Engineer at digiLab, an AI technology startup, where I worked from September 2023 to June 2025. I left to undertake a bikepacking journey from England to Bangladesh, during which I've continued to develop my skills through personal projects like findkairos.com and jaspercycles.com. I remain actively engaged in software development and am ready to return to full-time work.

## Question 13: Which of the following technologies or tools have you used before?

**Technologies I have professional experience with:**
- Python ✓
- JavaScript / TypeScript ✓
- Node.js ✓ (used for some internal tooling at digiLab)
- React ✓
- REST / GraphQL APIs ✓ (extensive REST API experience)
- Docker ✓
- AWS ✓ (extensive: ECS, Lambda, SQS, S3, EC2, ECR, CloudFront, Route53, SES, CloudFormation, Cognito, CloudWatch)
- Databases (SQL / NoSQL) ✓ (MongoDB, Redis)
- LLM or AI APIs ✓ (worked with various LLM APIs at digiLab)
- Agent frameworks (LangChain, LlamaIndex, etc.) ✓ (LangChain at digiLab)

**Technologies I do not have experience with:**
- Kubernetes (have not used in production, though familiar with concepts)
- GCP (no professional experience, though concepts transfer from AWS)
- Azure (no professional experience)

## Question 14: Describe an infrastructure or DevOps-related project you've worked on. What problem did it solve and what was your role?

At digiLab, I designed and implemented a node registry system that became a critical piece of our platform's re-architecture. The platform allowed users to build agentic workflows by connecting nodes together, where each node represented a distinct capability (ML models, RAG pipelines, chat functions, etc.).

**The Problem:**
As we re-architected the platform, each node became its own microservice with independent ECS deployments. This created several challenges: the frontend needed to contact every single node individually to gather metadata for the no-code builder UI, this data could become stale, and we had no centralized way to monitor node availability. We needed a single source of truth for node information and health status.

**My Solution:**
I built a node registry microservice that served as the central service discovery and monitoring system for our platform.

**Self-Registration Pattern:**
Nodes automatically registered themselves on startup using shared logic I built into a base Docker image. When deployed, each node would submit its interface definitions and metadata to the registry via a REST API. This approach ensured the registry always had current information without manual updates or configuration management.

**Interface Definition System:**
I established a developer workflow where node interfaces were defined in YAML files specifying inputs, outputs, version, description, display name, and credit cost. I wrote Makefiles that compiled these YAML definitions into Pydantic models for local development and implemented pre-commit hooks to ensure the generated models always matched the YAML source. This brought discipline to interface design and caught breaking changes early.

**Health Monitoring:**
The registry continuously polled the `/health` endpoint of each registered node using Python's asyncio to check all nodes concurrently. If a node failed three consecutive health checks, it was automatically deregistered and developers were notified via AWS SES. I chose the polling pattern over heartbeats because it gave the registry complete control over health check timing and could detect crashed nodes that couldn't send "I'm dying" messages.

**Frontend Integration:**
The registry exposed a `GET /nodes` endpoint that returned all node metadata, which powered the no-code builder UI. This data was also used by Zod to define type-safe node inputs in the React workflow canvas, ensuring the frontend and backend remained in sync.

**Deployment and Consistency:**
Everything was deployed via CI/CD pipelines, and the only way a node's information changed was through redeployment with updated YAML definitions. This ensured consistency - there was no configuration drift or manual updates to worry about. The registry used MongoDB for storage and was deployed on ECS with capacity to easily handle our target of under 100 nodes.

**Impact:**
This system solved the service discovery problem elegantly, reduced frontend complexity, provided operational visibility into node health, and created a clear contract for how nodes should be built. It became foundational infrastructure that enabled other teams to develop and deploy nodes independently while maintaining system-wide consistency.


## Question 15: Tell us about a time you had to debug a system failure, deployment issue, or performance problem. How did you approach identifying the root cause?

At digiLab, we used Modal (a serverless compute provider) for training ML models and running Bayesian optimization routines. One month, we noticed our cloud costs were abnormally high when reviewing the Modal dashboard.

**Initial Investigation:**
I started by searching Modal's logs for anomalies, specifically looking for long-running jobs. This revealed a job that had been running continuously for 24 hours with very high memory allocation, which immediately stood out as suspicious.

**Identifying the User and Context:**
The logs pointed to a specific user, so we contacted their assigned solutions engineer who reached out to gather information. The user had been batching optimization jobs and running them asynchronously, so he hadn't even noticed that several jobs were failing and restarting. He provided the code he was using, which was crucial for reproduction.

**Reproduction and Root Cause:**
I recreated the issue in our dev environment and monitored Modal's analytics dashboards. The problem became clear: the user was training a Gaussian Process model on a dataset with thousands of rows. GP models have quadratic memory complexity and simply don't scale to datasets that large. His optimization routine was trying to allocate more memory than Modal's infrastructure could provide.

The particularly problematic behavior was Modal's response to this: instead of failing immediately, it would restart the job and retry for up to 24 hours. This meant we were being charged for massive memory allocations on a job that could never succeed.

**The Fix:**
I implemented a multi-layered solution:

1. **Memory Limits:** Configured reasonable memory limits in our Modal deployment code to prevent runaway allocations
2. **Dataset Validation:** Added hard limits on dataset row and column sizes for model training to prevent users from attempting to train GP models on inappropriately large datasets
3. **Documentation:** Updated our user documentation to explain the computational constraints of different model types, particularly the scaling limitations of Gaussian Processes

We also contacted Modal about the retry behavior (they were a fairly new startup at the time), and while they gave generic responses about investigating it, they did provide free credits as an apology.

**Lessons Learned:**
This experience reinforced several debugging principles: start with the data (logs, metrics), reproduce systematically, and implement defense in depth. The fix wasn't just about preventing the specific bug but about adding validation layers to catch similar issues earlier. It also highlighted the importance of understanding the computational characteristics of ML algorithms when building platforms that let users run arbitrary workloads.

## Question 16: Tell us about a time you had to work with a database in a production or staging environment. What did you do and what tools or practices did you use?

At digiLab, I was responsible for designing and implementing the main user and resource database for our platform, which required a fundamental architectural shift to support collaboration features.

**The Problem:**
Our original system identified users by email and resources (datasets, models) by name, with no concept of shared ownership. We needed to introduce projects as a first-class concept, allowing users to collaborate by sharing resources within project workspaces. This required rethinking our entire data model.

**Database Architecture:**
I designed a project-centric schema in MongoDB where:
- Resources could belong to multiple projects (stored as a list of project IDs in each resource document)
- Users had project memberships with role-based permissions (admin vs. member)
- Only project admins could delete or update resources
- The database stored only metadata (name, type, size, owner, timestamps), with platform-agnostic references to actual storage locations (S3 paths, for example)

This metadata-first approach was crucial for frontend performance: when a user opened a Dataset node in the workflow builder, they'd see a dropdown populated from database metadata. Once they selected a dataset and connected it to a Model node, only the dataset ID was passed through the workflow, and the backend would retrieve the actual file from S3 when needed.

**Schema and Performance:**
I defined all schemas using Pydantic models for type safety and validation, then created indexes on key lookup fields (owner_id, project_id) to ensure fast queries for common operations like "get all of a user's projects" or "get all resources in this project."

**API Implementation:**
I built the entire service using FastAPI with pymongo's async driver, leveraging asyncio for concurrent database operations where possible. Access control was enforced at the API layer, where requests were validated against project membership and roles before executing database operations.

**Migration:**
While this was mostly greenfield work, I did handle migration from our old database with zero downtime using backup procedures and migration scripts to preserve existing user data while introducing the new project structure.

**Tools Used:**
- MongoDB with compound indexes
- Pydantic for schema definition and validation
- FastAPI for the REST API
- pymongo async driver for non-blocking database operations
- Python migration scripts with proper backup procedures

This work established the foundational data model that enabled collaboration features across the platform and set patterns for how other services should interact with shared resources.

## Question 17: Have you previously worked in a production environment (e.g., deployments, monitoring, on-call, automation, or cloud infrastructure)? If so, briefly describe what you worked on and the tools you used.

Yes, I have extensive production environment experience from my time at digiLab, where I was responsible for the full lifecycle of our services from development through production deployment and operations.

**Deployments:**
I designed and maintained our entire CI/CD pipeline using GitHub Actions and AWS services. Every merge to main triggered an automated deployment:
- Code testing and linting
- Docker image building and pushing to Amazon ECR
- CloudFormation stack updates for infrastructure changes
- Zero-downtime rolling deployments to ECS
- Lambda function updates via CloudFormation

I also handled versioning strategies, rollback procedures, and blue-green deployment patterns for critical services.

**Monitoring and Observability:**
I set up comprehensive monitoring using AWS CloudWatch:
- Custom metrics and dashboards for service health
- Log aggregation and structured logging across services
- Alarms for critical issues (error rates, latency spikes, resource utilization)
- Distributed tracing for debugging issues across microservices

I configured alerts to notify the team via email (SES) when critical thresholds were breached.

**Cloud Infrastructure:**
I managed our entire AWS infrastructure using Infrastructure as Code:
- Wrote and maintained CloudFormation templates for all resources
- Managed ECS clusters, task definitions, and services
- Configured Lambda functions, SQS queues, S3 buckets
- Set up CloudFront distributions and Route53 DNS
- Implemented Cognito for authentication
- Managed security groups, IAM roles, and policies

**Automation:**
Beyond deployment automation, I built internal tools to streamline operations:
- Scripts for common operational tasks (log analysis, data cleanup)
- Automated testing in CI pipeline
- Infrastructure validation and security scanning

**Tools Used:**
- AWS (ECS, Lambda, CloudWatch, CloudFormation, S3, SQS, ECR, CloudFront, Route53, Cognito, SES)
- Docker for containerization
- GitHub Actions for CI/CD
- Python scripts for automation
- Bash for operational scripts

**On-Call Experience:**
While we didn't have a formal on-call rotation due to our small team size, I was often the first point of contact for production issues given my infrastructure knowledge. I helped establish runbooks for common issues and implemented monitoring that would catch problems before they impacted users.

**Personal Projects:**
I've also deployed and managed production infrastructure for my personal projects (findkairos.com, jaspercycles.com) using similar AWS patterns: Lambda functions, S3 + CloudFront for static hosting, automated deployments via GitHub Actions. This independent work demonstrates my ability to own the full stack without supervision.

## Question 18: If you have a GitHub, portfolio, or project link you'd like to share, include it here.

**GitHub:** github.com/jacantwell

**LinkedIn:** linkedin.com/in/jasper-cantwell-gill

**Personal Projects:**

**findkairos.com** - A full-stack web application for connecting bikepackers worldwide
- Backend: Python FastAPI with MongoDB (including GeoSpatial indexing), deployed as serverless functions on AWS Lambda
- Frontend: Next.js with Mapbox integration, statically hosted on AWS (S3 + CloudFront)
- Features: Automated OpenAPI TypeScript client generation published to npm, token-based authentication, scalable database schema for user journey tracking
- Demonstrates: Backend API design, serverless architecture, geospatial queries, frontend development, automated deployment pipelines

**jaspercycles.com** - Personal project tracking my bikepacking journey in real-time
- React + Vite frontend integrating with Strava API
- Deployed as static site on AWS (S3 + CloudFront) with automated deployment pipeline
- Demonstrates: API integration, React development, automated deployment

These projects showcase my ability to independently build and deploy production-quality full-stack applications, and they represent work I've done while traveling with limited resources, which demonstrates my self-motivation and problem-solving abilities.

**Contact Information:**
- Email: jasper66018@gmail.com
- WhatsApp: +447423781157 (best for video calls given my current travel situation)

I'm currently traveling but am fully available for remote interviews and can arrange video calls at your convenience.
