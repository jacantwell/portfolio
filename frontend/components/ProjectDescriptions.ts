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

`;

export const gitlogDescription = `

I've always been terrible at keeping track of my accomplishments at work. Everyone says you should maintain a log of what you've done for when you need to update your CV or go for a promotion, but I never actually do it. Then I realized that 99% of my work is already tracked on GitHub through my commits and pull requests. So why not just use that data?

This project pulls your GitHub commit and PR history using the GitHub REST API and uses LLMs to turn it into a readable summary of everything you've worked on. It's basically an automated way to document your accomplishments without having to remember to write them down. Plus, knowing that this tool exists has actually inspired me to write better commit messages and create higher quality PRs, since garbage in means garbage out.

`;

export const portfolioDescription =`

AI chatbot portfolio website that provides users info about me using RAG.
`