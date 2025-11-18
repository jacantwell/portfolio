"use client";

import { useState } from "react";
import {
  Menu,
  Phone,
  Mail,
  Github,
  ExternalLink,
  Download,
} from "lucide-react";
import { Button } from "@/components/retroui/Button";
import { Card } from "./retroui/Card";
import { Accordion } from "./retroui/Accordion";
import Link from "next/link";
import { Dialog } from "@/components/retroui/Dialog";
import { Text } from "./retroui/Text";
import ReactMarkdown from "react-markdown";
import {
  jaspercyclesDescription,
  s3mobileDescription,
  gitlogDescription,
  kairosDescription,
  portfolioDescription,
} from "./ProjectDescriptions";

interface Project {
  name: string;
  displayName: string;
  description: string;
  websiteUrl?: string;
  githubUrl?: string;
}

const projects: Project[] = [
  {
    name: "portfolio",
    displayName: "Portfolio Website",
    description: portfolioDescription,
    websiteUrl: undefined,
    githubUrl: "https://github.com/jacantwell/portfolio",
  },
  {
    name: "kairos",
    displayName: "findkairos.com",
    description: kairosDescription,
    websiteUrl: "https://findkairos.com",
    githubUrl: "https://github.com/jacantwell/kairos-web",
  },
  {
    name: "jaspercycles",
    displayName: "jaspercycles.com",
    description: jaspercyclesDescription,
    websiteUrl: "https://jaspercycles.com",
    githubUrl: "https://github.com/jacantwell/jaspercycles",
  },
  {
    name: "s3-mobile",
    displayName: "s3 Mobile App",
    description: s3mobileDescription,
    githubUrl: "https://github.com/jacantwell/s3-mobile",
  },
  {
    name: "gitLog",
    displayName: "gitLog",
    description: gitlogDescription,
    githubUrl: "https://github.com/jacantwell/git-log",
  },
];

export function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => setIsOpen(!isOpen);

  return (
    <>
      {isOpen ? (
        <div></div>
      ) : (
        <Button
          variant="secondary"
          onClick={toggleSidebar}
          className="fixed left-4 bottom-4 md:left-4 md:top-4 z-50 flex h-10 w-fit items-center justify-center font-bold shadow-lg"
        >
          Menu
        </Button>
      )}

      {/* Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 z-30 bg-black/50 backdrop-blur-sm"
          onClick={toggleSidebar}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`fixed left-0 top-0 z-40 h-screen w-75 transform shadow-2xl transition-transform duration-300 ease-in-out ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="flex h-full flex-col overflow-hidden">
          <Card className="flex-1 overflow-y-auto pr-1 justify-between items-start shadow-none hover:shadow-none outline-0">
            <Card.Header className="pb-0">
              <Card.Title className="pb-0 text-4xl font-bold">
                Jasper Cantwell
              </Card.Title>
            </Card.Header>
            <Card.Header className="pt-0 pb-0 text-xl">
              Full-Stack Software Engineer
            </Card.Header>
            <Card.Content className="pb-0 pt-2 mb-0">
              <Button className="w-full px-2 items-center">
                <a
                  href="mailto:jasper66018@gmail.com"
                  className="flex items-center gap-3 rounded-lg text-sm"
                >
                  <Mail className="h-4 w-4" />{" "}
                  <span>jasper66018@gmail.com</span>
                </a>
              </Button>
            </Card.Content>

            <Card.Content className="pb-0 pt-2 mb-0">
              <Button className="w-full px-2 items-center">
                <div className="flex items-center gap-3 rounded-lg text-sm">
                  <Phone className="h-4 w-4" /> <span>+44 74237 81157</span>
                </div>
              </Button>
            </Card.Content>

            <Card.Content className="pb-0">
              <a
                href="/assets/Jasper_Cantwell_CV.pdf"
                download="Jasper_Cantwell_CV.pdf"
              >
                <Button
                  variant="secondary"
                  className="w-full px-2 items-center"
                >
                  <div className="flex items-center gap-3 rounded-lg text-sm">
                    <Download className="h-4 w-4" /> <span>Download CV</span>
                  </div>
                </Button>
              </a>
            </Card.Content>
            <Card.Header className="pb-0">
              <Card.Title>Projects</Card.Title>
            </Card.Header>

            <Card.Content className="flex justify-between items-center pt-0 pb-4">
              <Accordion type="single" collapsible className="space-y-4 w-full">
                {projects.map((project) => (
                  <div key={project.name} className="relative">
                    <Accordion.Item value={project.name}>
                      <Accordion.Header>{project.name}</Accordion.Header>
                      <Accordion.Content>
                        <Dialog>
                          <Dialog.Trigger asChild>
                            <Button className="w-full h-fit">
                              <div className="flex items-center gap-2 rounded text-xs">
                                <ExternalLink className="h-3 w-3" />{" "}
                                <span>Description</span>
                              </div>
                            </Button>
                          </Dialog.Trigger>
                          <Dialog.Content className="max-w-2xl max-h-[85vh] overflow-hidden">
                            <Dialog.Header>
                              <Text as="h5">{project.name}</Text>
                            </Dialog.Header>
                            <div className="overflow-y-auto max-h-[calc(85vh-4rem)] px-4 pb-4 mt-2">
                              <article className="prose prose-sm dark:prose-invert max-w-none">
                                <ReactMarkdown>
                                  {project.description}
                                </ReactMarkdown>
                              </article>
                            </div>
                          </Dialog.Content>
                        </Dialog>

                        {project.websiteUrl && (
                          <Link
                            href={project.websiteUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                          >
                            <Button className="w-full h-fit mt-2">
                              <div className="flex items-center gap-2 rounded text-xs">
                                <ExternalLink className="h-3 w-3" />{" "}
                                <span>Visit Website</span>
                              </div>
                            </Button>
                          </Link>
                        )}
                        {project.githubUrl && (
                          <Link
                            href={project.githubUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                          >
                            <Button className="w-full h-fit mt-2">
                              <div className="flex items-center gap-2 rounded text-xs">
                                <Github className="h-3 w-3" />{" "}
                                <span>View on Github</span>
                              </div>
                            </Button>
                          </Link>
                        )}
                      </Accordion.Content>
                    </Accordion.Item>
                  </div>
                ))}
              </Accordion>
            </Card.Content>
          </Card>
        </div>
      </aside>
    </>
  );
}