---
type: application
document: application_questions
company: Locai Labs
role: Backend Engineer / AI Systems
date: 2025-11-12
tags: [backend, ai_systems, agentic_tools, production_experience, cloud_infrastructure]
question_topics:
  - motivation
  - experience_years
  - ai_enthusiasm
  - backend_projects
  - research_projects
  - background
  - fast_paced_environment
  - distributed_systems
  - learning_style
  - work_environment
  - testing_practices
  - production_operations
  - portfolio
technologies_mentioned:
  languages: [Python, TypeScript, JavaScript, C]
  frameworks: [FastAPI, LangChain, TensorFlow, PyTorch, BoTorch, React, Next.js, Vite]
  cloud: [AWS Lambda, AWS ECS, AWS SQS, AWS CloudWatch, AWS Cognito, AWS S3, AWS CloudFront, AWS Route53, AWS SES, CloudFormation, ECR]
  databases: [MongoDB]
  tools: [Docker, GitHub Actions, Pydantic, pytest]
  ml_techniques: [Gaussian Processes, Bayesian Optimization, Neural Networks, RAG, Uncertainty Quantification]
---

# Job Application Responses

## Question 5: Why do you want to work at Locai Labs?

### Answer
What draws me to Locai Labs is the opportunity to contribute to foundational AI development from within the UK. Having spent the past two years building ML workflow platforms and agentic systems, I've seen firsthand how critical the underlying infrastructure and engineering excellence are to creating truly capable AI systems. Your mission to advance cutting-edge AI through deep technical innovation resonates with my own approach to engineering.

I'm particularly excited about Locai Labs' focus on building world-class LLMs with an emphasis on cost and efficiency alongside capability. At digiLab, I worked on systems where computational efficiency directly impacted our ability to serve clients, so I appreciate the engineering challenges involved in optimizing large-scale AI systems. The chance to work on foundational models, agentic applications, and developer tools that enable intelligent automation aligns perfectly with where I want to take my career.

Your small, highly technical team structure also appeals to me. At digiLab, I was selected for a scout team with the CEO and CTO to design our event-driven microservice architecture, and I thrived in that environment where individual contributions directly shaped the product. The fact that every engineer at Locai Labs helps define architecture and product direction is exactly the kind of ownership and impact I'm looking for.

**Key Points:**
- 2 years experience building ML workflow platforms and agentic systems
- Appreciation for computational efficiency in AI systems
- Experience with architectural design in small teams
- Seeking high-impact, ownership-driven environment

---

## Question 6: How many years of professional software engineering experience do you have?

### Answer
2 years (September 2023 - June 2025 at digiLab)

---

## Question 7: What excites you about building AI systems and agentic tools?

### Answer
What excites me most about building AI systems is the intersection of complex engineering challenges and tangible real-world impact. During my time at digiLab, I worked on an ML workflow platform that used LangChain to provide agentic solutions, and I found the orchestration challenges fascinating. There's something uniquely satisfying about designing systems that can reason, plan, and execute tasks autonomously while remaining reliable and maintainable at scale.

The technical depth required is what really draws me in. Building production-ready agentic systems isn't just about integrating an LLM API; it requires thoughtful architecture around state management, error handling, workflow orchestration, and observability. I love problems that span multiple layers of the stack, from designing efficient data pipelines and event-driven architectures to implementing robust authentication and monitoring systems.

I'm also excited by the rapid evolution of the field. The shift from simple prompt-response patterns to sophisticated multi-agent systems with tool use and reasoning capabilities opens up entirely new categories of applications. Having extended our internal ML library with Gaussian Process models for uncertainty quantification, I appreciate how important it is to understand not just what an AI system outputs, but how confident we can be in those outputs. Building systems that are both powerful and trustworthy is a challenge I find deeply motivating.

**Key Points:**
- Hands-on experience with LangChain for agentic solutions
- Focus on production-readiness: state management, error handling, orchestration, observability
- Experience with Gaussian Process models for uncertainty quantification
- Full-stack perspective from data pipelines to authentication

---

## Question 8: Describe a backend or AI-related project you've worked on that you're proud of. What was your role and what technologies did you use?

### Answer
One of my most impactful projects at digiLab was rapidly bringing a complex microservice from concept to production in just 2 months, despite constantly shifting requirements. This service was a core component of our ML workflow platform and needed to handle user authentication, integrate with our event-driven architecture, and provide analytics capabilities.

I was the lead engineer responsible for the entire backend implementation.

**Technical Stack:**
- Python FastAPI for the REST API with Pydantic for robust data validation
- AWS Cognito for token-based authentication and user management
- AWS CloudWatch for user analytics and operational monitoring
- AWS SQS for event-driven communication with other microservices
- Docker containerization deployed on AWS ECS
- CloudFormation for infrastructure as code
- GitHub Actions for CI/CD automation

**Challenges:**
The challenge was building something production-ready while requirements were evolving based on client feedback. I implemented a modular architecture with clear separation of concerns, which allowed me to adapt quickly without accumulating technical debt. The authentication layer was particularly complex, as it needed to support multiple user types with different permission levels while integrating seamlessly with our existing infrastructure.

**Outcomes:**
What I'm most proud of is that despite the time pressure and shifting requirements, the service launched successfully and has been running reliably in production. The modular design I implemented also made it significantly easier for data scientists on the team to contribute features independently, which accelerated our overall development velocity. This project taught me a lot about balancing speed with quality and the importance of clear API design in distributed systems.

**Key Points:**
- Lead engineer role with full backend ownership
- 2-month timeline with shifting requirements
- Event-driven microservice architecture
- Production-ready with modular design enabling team velocity

---

## Question 9: Have you previously completed any AI-related personal or research projects? (If yes, briefly describe.)

### Master's Thesis (2023)
**Title:** The Application of Machine Learning to the Inverse Scattering Problem

Built neural networks using TensorFlow to solve inverse problems in physics, gaining hands-on experience with the challenges of applying ML to real-world scientific problems where data quality and physical constraints matter.

### Professional ML Work at digiLab
Extended our internal machine learning library with Gaussian Process models using PyTorch and BoTorch, which improved uncertainty quantification for production ML workflows. This involved implementing Bayesian optimization techniques that helped our clients make better decisions based on model predictions.

### Production Agentic Systems
For digiLab's newest product, I was responsible for taking our CTO's LangChain prototype code and transforming it into a production-ready, cloud-native platform. This was a core product engineering challenge that involved more than just "making it work" - I had to design robust interfaces, implement comprehensive error handling, and adapt the code for cloud environments where constraints like file loading for RAG pipelines work fundamentally differently than on local machines.

I built the microservice backend that powered our no-code AI platform, using LangChain agents and tools to enable users to build sophisticated workflows without writing code. The technical challenges included making the system safe and reliable for end users - implementing proper error boundaries, adding comprehensive pytest test coverage, and designing APIs that could handle the unpredictable nature of LLM outputs gracefully.

**Real-World Use Cases:**
- Agentic RAG workflows for nuclear engineers
- AI triage systems for the healthcare company KOYO
- ML model integration where agents could suggest and comment on Gaussian Process model parameters
- Customizable message-based chat functions

This work gave me deep practical experience with the challenges of building production agentic systems: managing state across agent interactions, handling tool execution failures, and ensuring the system remained reliable even when LLMs produced unexpected outputs.

**Key Points:**
- Research background: ML for inverse problems in physics
- Production ML: Gaussian Processes, Bayesian optimization, uncertainty quantification
- Agentic systems: LangChain, RAG pipelines, production-ready architecture
- Real-world deployments in nuclear engineering and healthcare

---

## Question 10: Is there anything else you'd like us to know about your background, experience, or interests?

### Physics Background
My physics degree has fundamentally shaped how I approach software engineering. The mathematical rigor and analytical problem-solving skills I developed translate directly to system design and debugging complex distributed systems. My thesis on inverse problems using ML gave me a solid foundation in understanding the theoretical underpinnings of machine learning, not just the practical implementation.

### Mentorship and Knowledge Sharing
I've consistently received positive feedback for being approachable and supportive with team members. At digiLab, I helped onboard graduate hires and delivered technical presentations to help the team level up. I believe strong teams are built on knowledge sharing, and I enjoy helping others grow.

### Advocacy and Leadership
I served as the employee association representative at digiLab, leading discussions with founders about workplace improvements. This experience taught me how to advocate effectively for team needs while understanding business constraints, and it resulted in tangible improvements like secured office amenities and the formation of an internal AI ethics committee.

### Current Journey
I'm currently on a bikepacking trip from England toward Bangladesh, and I've been building and deploying software projects along the way. This demonstrates my genuine passion for software development (I literally can't stop coding even while cycling across continents!) and my ability to deliver production-quality work independently with minimal resources.

### Open Source and Community
My GitHub profile (github.com/jacantwell) showcases my personal projects and coding approach. I believe in building in public and contributing back to the developer community.

**Key Points:**
- Physics background: strong analytical and problem-solving foundation
- Team contributor: mentorship, knowledge sharing, onboarding
- Leadership: employee representative, workplace advocacy
- Self-motivated: building projects while traveling
- Community-oriented: open source, building in public

---

## Question 11: Our environment is fast-moving and hands-on. Engineers often take ownership of both infrastructure and backend services. What interests you about working in this kind of environment?

### Answer
This type of environment is exactly where I thrive. At digiLab, I took full ownership of services from infrastructure provisioning to production deployment, and I genuinely enjoyed the end-to-end responsibility.

### Direct Connection Between Decisions and Outcomes
What interests me most is the direct connection between decisions and outcomes. When you own both infrastructure and application code, you can make architectural choices that optimize for the specific needs of your system rather than working within rigid constraints. For example, when designing our microservice architecture at digiLab, I could choose the right AWS services (Lambda vs ECS, SQS vs SNS) based on actual usage patterns and cost considerations, then implement the infrastructure as code alongside the application logic. This holistic approach leads to better systems.

### Learning Opportunities
I also appreciate the learning opportunities. Managing infrastructure forces you to think about operational concerns like monitoring, logging, scalability, and cost optimization from day one. Deploying my own services taught me to write more maintainable code because I knew I'd be the one debugging it at 2am if something went wrong. That ownership mindset leads to better engineering practices.

### Fast-Paced Performance
The fast-paced aspect is equally appealing. I performed well under pressure when I built our authentication microservice in 2 months with shifting requirements. The key is staying pragmatic: shipping something good quickly is better than pursuing perfection slowly. In a startup environment, you need to balance technical excellence with business needs, and I enjoy that challenge.

### Continuous Growth
Finally, the hands-on nature means you're always learning. At digiLab, I went from basic Docker knowledge to designing entire CloudFormation templates and CI/CD pipelines. When you take ownership of the full stack, every problem becomes an opportunity to deepen your expertise.

**Key Points:**
- Full ownership experience: infrastructure + application code
- Architectural decision-making based on real-world constraints
- Operational mindset: monitoring, maintainability, debugging
- Pragmatic approach: balance speed with quality
- Proven fast-paced performance: 2-month microservice delivery

---

## Question 12: Have you worked with distributed systems, microservices, or event-driven architectures? If yes, briefly describe your experience.

### Answer
Yes, this has been a core focus of my work at digiLab. I was selected for a scout team with the CEO, CTO, and lead architect to design our long-term event-driven microservice architecture. This architecture enabled modular development that helped data scientists contribute 100% faster.

### Microservices Architecture
I designed and built multiple microservices that communicated via AWS SQS, each with clearly defined responsibilities and APIs. Services handled authentication, data processing, ML model orchestration, and user interface backends. The key challenge was maintaining loose coupling while ensuring reliable communication patterns.

### Event-Driven Patterns
Our architecture heavily relied on event-driven patterns:
- Used AWS SQS for asynchronous message passing between services
- Implemented event sourcing patterns for audit trails
- Designed idempotent message handlers to handle retries gracefully
- Built dead letter queues for failed message handling

### Distributed System Challenges
I dealt with typical distributed systems problems:
- **Eventual consistency:** Designed systems that could handle data being out of sync across services
- **Service discovery:** Configured service mesh patterns for inter-service communication
- **Monitoring and debugging:** Implemented distributed tracing to follow requests across service boundaries
- **Failure modes:** Built circuit breakers and graceful degradation when dependencies failed
- **Data consistency:** Designed transaction boundaries and compensation strategies

### Infrastructure
All of this ran on AWS infrastructure:
- ECS for container orchestration
- Lambda for serverless functions
- SQS for message queues
- CloudWatch for distributed logging and monitoring
- CloudFormation for infrastructure as code managing all resources

### Outcomes
The modular architecture allowed different team members to work independently on separate services without blocking each other. We could deploy services independently, scale them based on their specific load patterns, and debug issues in isolation. This was crucial for our small team's velocity.

**Key Points:**
- Architectural design experience: scout team for event-driven microservices
- Hands-on implementation: multiple microservices with AWS SQS communication
- Distributed systems expertise: eventual consistency, failure modes, monitoring
- Real impact: 100% faster contribution velocity for data scientists

---

## Question 13: How do you typically approach learning new technologies or frameworks when needed for a project?

### Answer
I'm a strong believer in learning by doing, but with structure. When I need to learn a new technology, I typically follow this approach:

### Initial Research Phase
I start with official documentation to understand the core concepts and design philosophy. I've found that understanding why a technology was built and what problems it solves helps me use it more effectively. I'll also look at comparison articles to understand where it fits in the ecosystem.

### Hands-On Experimentation
Next, I build something small but meaningful. Not just a "hello world," but a miniature version of what I'll actually need. For example, when learning FastAPI at digiLab, I built a simple API with authentication and database connections before integrating it into our production system. This helps me identify gotchas early.

### Deep Dive on Critical Paths
Once I understand the basics, I focus on the specific areas that will be critical for my use case. If I'm building a high-throughput service, I'll dive deep into performance optimization. If it's a data processing pipeline, I'll focus on error handling and retry logic. This targeted learning is more efficient than trying to master everything at once.

### Learning from Production
Some of the best learning happens when things break. I keep detailed notes when I encounter issues and make sure I understand the root cause, not just the fix. This builds mental models that help me avoid similar issues in the future.

### Examples from My Experience
- **AWS Infrastructure:** I went from basic Docker knowledge to designing complex CloudFormation templates by iteratively building increasingly sophisticated deployments. Each service taught me something new.
- **GPU Programming:** During my research internship, I learned CUDA by first understanding parallel computing concepts, then working through progressively complex kernel implementations, ultimately achieving 60% performance improvements.
- **LangChain:** For our agentic platform, I started with the documentation, built simple agent examples, then scaled up to production RAG pipelines. The key was understanding the abstractions before trying to customize them.

### Continuous Learning
I also maintain this approach outside of work requirements. My personal projects (findkairos.com, jaspercycles.com) are opportunities to learn new technologies like MongoDB's geospatial queries or Next.js's static site generation without the pressure of production deadlines.

**Key Points:**
- Structured approach: documentation → hands-on → targeted deep dive → production learning
- Learning by building meaningful projects, not just tutorials
- Focus on understanding underlying concepts and design philosophy
- Track learnings from production issues to build mental models
- Continuous learning through personal projects

---

## Question 14: What kind of team or work environment do you prefer? (e.g., startup vs. corporate, remote vs. in-person, highly collaborative vs. independent)

### Answer
Based on my experience at digiLab, I've learned that I thrive in a startup environment with a highly technical, collaborative team. Here's what works best for me:

### Startup Over Corporate
I prefer the startup environment because individual contributions have direct, visible impact. At digiLab, I could propose an architectural change in the morning and have it deployed by afternoon if it made sense. That rapid iteration and ownership is energizing. I also appreciate that in startups, you're forced to be pragmatic about tradeoffs rather than following rigid processes.

### Balance of Collaboration and Autonomy
I work best with a balance. I enjoy collaborative architecture discussions and design reviews where we can debate approaches and learn from each other's perspectives. Being on the scout team at digiLab, working directly with the CEO and CTO on system design, was incredibly valuable for my growth.

However, I also value having ownership of specific areas where I can make decisions independently and execute without constant check-ins. The trust to own a service end-to-end, from architecture to deployment, is important to me. I'm self-motivated and can drive projects forward without much direction once the goals are clear.

### Remote vs. In-Person
I've worked successfully in both settings. At digiLab, we had a mix of in-office and remote work. I found that being in the office was valuable for spontaneous technical discussions and building team relationships, especially when onboarding. But I'm also productive remotely, as evidenced by the fact that I'm currently building production-quality software while traveling across continents.

The key is having good communication practices. I'm proactive about documenting decisions, writing clear code comments, and keeping the team updated on progress. I'm comfortable with video calls, async communication via Slack, and detailed technical writing.

### Highly Technical Teams
I strongly prefer working with technically deep teams where I can learn from colleagues and be challenged. At digiLab, being able to discuss ML algorithms with our data scientists or debate architectural patterns with the CTO made me a better engineer. I want to work with people who care deeply about code quality, system design, and continuous improvement.

### Ideal Environment Summary
Small, technical startup with significant ownership and autonomy, balanced with collaborative architecture discussions. Mix of remote flexibility and in-person collaboration opportunities. Team that values engineering excellence and continuous learning.

**Key Points:**
- Preference: technical startup environment with direct impact
- Balance: collaborative design + autonomous execution
- Flexible: productive both remote and in-person
- Team: highly technical colleagues who value excellence
- Current demonstration: building production software while traveling

---

## Question 15: How do you approach writing tests for your code? What testing practices do you typically follow?

### Answer
Testing is something I've become increasingly disciplined about, especially after seeing the value it provides in production systems. My approach has evolved from "testing when I remember" to "testing as part of the development workflow."

### Testing Philosophy
I view tests as a tool for confidence and maintainability, not just coverage metrics. The goal is to catch bugs before they reach production and to make refactoring safer. I focus on testing behavior rather than implementation details, which makes tests more resilient to code changes.

### Test Coverage Strategy
I typically follow this hierarchy:

**Unit Tests (Most):**
- Test individual functions and methods in isolation
- Focus on edge cases, error conditions, and business logic
- Use pytest at digiLab with fixtures for common test data
- Mock external dependencies (APIs, databases) to keep tests fast and deterministic
- Aim for comprehensive coverage of critical paths and edge cases

**Integration Tests (Some):**
- Test interactions between components
- Verify database queries, API endpoints, and service integrations
- Use test databases or Docker containers for realistic testing environments
- Slower than unit tests but crucial for catching integration issues

**End-to-End Tests (Few):**
- Test critical user workflows through the entire stack
- Expensive to maintain but valuable for core functionality
- Focus on happy paths and critical error scenarios

### Specific Practices
At digiLab, I implemented several testing practices:

**API Testing:**
- Used pytest with FastAPI's TestClient to test endpoints
- Validated request/response schemas using Pydantic
- Tested authentication flows, permission checks, and error responses
- Mocked AWS services (SQS, Cognito) using moto library

**Error Handling Tests:**
- Explicitly tested failure modes and error boundaries
- Verified that errors propagated correctly through the system
- Tested retry logic and circuit breaker behavior

**Test-Driven Development (Selectively):**
For complex algorithms or critical business logic, I sometimes use TDD. Writing tests first helps clarify requirements and design better interfaces. For example, when implementing Gaussian Process models, I wrote tests for expected behavior before implementation.

**CI Integration:**
All tests run automatically in CI (GitHub Actions) before deployment. Failed tests block merges. This catches issues early and maintains code quality across the team.

### Real-World Example
When building our authentication microservice, I wrote comprehensive tests for:
- Token generation and validation
- Permission checks for different user types
- Integration with AWS Cognito
- Error handling when Cognito was unavailable
- Race conditions in concurrent authentication requests

These tests caught several subtle bugs during development and gave me confidence to refactor the authentication layer later without fear of breaking existing functionality.

### Areas for Improvement
I'll admit I'm still improving at:
- Writing more comprehensive integration tests
- Better test data management strategies
- Performance testing and load testing practices

I view testing as a skill that requires continuous refinement, and I'm always looking to learn better practices from experienced engineers.

**Key Points:**
- Testing philosophy: confidence and maintainability over coverage metrics
- Practical hierarchy: comprehensive unit tests, selective integration tests, focused E2E tests
- Hands-on experience: pytest, FastAPI TestClient, mocking AWS services
- CI integration: automated testing in deployment pipelines
- Real-world application: comprehensive testing of authentication microservice
- Growth mindset: continuously improving testing practices

---

## Question 16: Can you describe your experience with version control and collaborative development workflows (e.g., Git, pull requests, code reviews)?

### Answer
Git and collaborative development workflows have been central to my daily work at digiLab. I have strong experience with modern development practices.

### Git Proficiency
I'm comfortable with Git beyond basic operations:
- Branching strategies (we used feature branches and main)
- Interactive rebasing for clean commit history
- Cherry-picking for selective commits
- Merge conflict resolution
- Git hooks for pre-commit checks

I maintain clean, atomic commits with descriptive messages because I know that commit history is documentation for future developers (including future me).

### Pull Request Workflow
At digiLab, we followed a standard PR workflow:
1. Create feature branch from main
2. Develop feature with regular commits
3. Push branch and open PR with description of changes
4. Automated CI runs tests and linting
5. Request review from team members
6. Address feedback and iterate
7. Merge when approved and CI passes

### Code Review Practices

**As a Reviewer:**
I focus on:
- Correctness and potential bugs
- Code clarity and maintainability
- Architectural fit within the system
- Test coverage
- Performance considerations

I try to be constructive in my feedback, explaining why something might be improved rather than just pointing out issues. I've learned that good code reviews are about knowledge sharing, not gatekeeping.

**As a Reviewee:**
I'm receptive to feedback and view code reviews as learning opportunities. I've had my code significantly improved by teammates who caught issues I missed or suggested better approaches. I'm not precious about my code - the goal is the best solution, not my solution.

### Collaborative Development
Beyond PRs and reviews, effective collaboration requires:
- Clear communication about what you're working on
- Documenting architectural decisions
- Raising blockers early
- Being available to help teammates
- Keeping PRs reasonably sized for easier review

At digiLab, I helped establish practices like:
- PR templates to ensure consistent descriptions
- Required reviews before merging
- Automated linting and formatting to reduce bikeshedding
- Documentation of major architectural decisions in markdown files

### Personal Projects
Even for my solo projects, I maintain good Git practices:
- Descriptive commit messages
- Logical commit organization
- Branching for features
- GitHub Actions for CI/CD

This discipline has saved me multiple times when I needed to understand what changed or revert problematic commits.

### Real-World Impact
Good version control practices enabled our team to:
- Work in parallel without stepping on each other
- Review and learn from each other's code
- Maintain high code quality standards
- Deploy confidently knowing changes were reviewed
- Debug issues by examining commit history

**Key Points:**
- Proficient with Git: branching, rebasing, conflict resolution, clean history
- Standard PR workflow: feature branches, CI integration, review process
- Code review experience: both giving and receiving constructive feedback
- Collaborative practices: communication, documentation, team coordination
- Disciplined approach even in personal projects
- Real impact: enabled parallel development and maintained code quality

---

## Question 17: Have you previously worked in a production environment (e.g., deployments, monitoring, on-call, automation, or cloud infrastructure)? If so, briefly describe what you worked on and the tools you used.

### Answer
Yes, I have extensive production environment experience from my time at digiLab, where I was responsible for the full lifecycle of our services from development through production deployment and operations.

### Deployments
I designed and maintained our entire CI/CD pipeline using GitHub Actions and AWS services. Every merge to main triggered an automated deployment:
- Code testing and linting
- Docker image building and pushing to Amazon ECR
- CloudFormation stack updates for infrastructure changes
- Zero-downtime rolling deployments to ECS
- Lambda function updates via CloudFormation

I also handled versioning strategies, rollback procedures, and blue-green deployment patterns for critical services.

### Monitoring and Observability
I set up comprehensive monitoring using AWS CloudWatch:
- Custom metrics and dashboards for service health
- Log aggregation and structured logging across services
- Alarms for critical issues (error rates, latency spikes, resource utilization)
- Distributed tracing for debugging issues across microservices

I configured alerts to notify the team via email (SES) when critical thresholds were breached.

### Cloud Infrastructure
I managed our entire AWS infrastructure using Infrastructure as Code:
- Wrote and maintained CloudFormation templates for all resources
- Managed ECS clusters, task definitions, and services
- Configured Lambda functions, SQS queues, S3 buckets
- Set up CloudFront distributions and Route53 DNS
- Implemented Cognito for authentication
- Managed security groups, IAM roles, and policies

### Automation
Beyond deployment automation, I built internal tools to streamline operations:
- Scripts for common operational tasks (log analysis, data cleanup)
- Automated testing in CI pipeline
- Infrastructure validation and security scanning

### Tools Used
- **AWS:** ECS, Lambda, CloudWatch, CloudFormation, S3, SQS, ECR, CloudFront, Route53, Cognito, SES
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Scripting:** Python, Bash
- **Version Control:** Git/GitHub

### On-Call Experience
While we didn't have a formal on-call rotation due to our small team size, I was often the first point of contact for production issues given my infrastructure knowledge. I helped establish runbooks for common issues and implemented monitoring that would catch problems before they impacted users.

### Personal Projects
I've also deployed and managed production infrastructure for my personal projects (findkairos.com, jaspercycles.com) using similar AWS patterns: Lambda functions, S3 + CloudFront for static hosting, automated deployments via GitHub Actions. This independent work demonstrates my ability to own the full stack without supervision.

**Key Points:**
- Full CI/CD ownership: GitHub Actions, Docker, ECR, automated deployments
- Comprehensive monitoring: CloudWatch dashboards, alarms, distributed tracing
- Infrastructure as Code: CloudFormation templates for all AWS resources
- Production operations: deployments, rollbacks, incident response
- Automation: scripts for operational tasks, CI pipeline integration
- Personal demonstration: independently deployed and managed production infrastructure

---

## Question 18: If you have a GitHub, portfolio, or project link you'd like to share, include it here.

### GitHub
[github.com/jacantwell](https://github.com/jacantwell)

### LinkedIn
[linkedin.com/in/jasper-cantwell-gill](https://linkedin.com/in/jasper-cantwell-gill)

### Personal Projects

#### findkairos.com
**Full-stack web application for connecting bikepackers worldwide**

**Backend:**
- Python FastAPI with MongoDB (including GeoSpatial indexing)
- Deployed as serverless functions on AWS Lambda

**Frontend:**
- Next.js with Mapbox integration
- Statically hosted on AWS (S3 + CloudFront)

**Key Features:**
- Automated OpenAPI TypeScript client generation published to npm
- Token-based authentication
- Scalable database schema for user journey tracking

**Demonstrates:**
- Backend API design
- Serverless architecture
- Geospatial queries
- Frontend development
- Automated deployment pipelines

#### jaspercycles.com
**Personal project tracking my bikepacking journey in real-time**

**Stack:**
- React + Vite frontend integrating with Strava API
- Deployed as static site on AWS (S3 + CloudFront) with automated deployment pipeline

**Demonstrates:**
- API integration
- React development
- Automated deployment

### About These Projects
These projects showcase my ability to independently build and deploy production-quality full-stack applications, and they represent work I've done while traveling with limited resources, which demonstrates my self-motivation and problem-solving abilities.

### Contact Information
- **Email:** jasper66018@gmail.com
- **WhatsApp:** +447423781157 (best for video calls given my current travel situation)

I'm currently traveling but am fully available for remote interviews and can arrange video calls at your convenience.