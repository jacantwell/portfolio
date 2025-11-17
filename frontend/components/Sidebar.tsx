"use client";

import { useState } from "react";
import {
  Menu,
  X,
  Phone,
  Mail,
  Github,
  ExternalLink,
  Download,
  Folder,
} from "lucide-react";

interface Project {
  name: string;
  displayName: string;
  description: string;
  websiteUrl?: string;
  githubUrl?: string;
}

const projects: Project[] = [
  {
    name: "findkairos",
    displayName: "findkairos.com",
    description: "Web app connecting bikepackers worldwide",
    websiteUrl: "https://findkairos.com",
    githubUrl: "https://github.com/jacantwell/findkairos",
  },
  {
    name: "jaspercycles",
    displayName: "jaspercycles.com",
    description: "Real-time bikepacking journey tracker",
    websiteUrl: "https://jaspercycles.com",
    githubUrl: "https://github.com/jacantwell/jaspercycles",
  },
  {
    name: "portfolio",
    displayName: "Portfolio Website",
    description: "This portfolio website with AI chat",
    websiteUrl: undefined,
    githubUrl: "https://github.com/jacantwell/portfolio",
  },
];

export function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => setIsOpen(!isOpen);

  return (
    <>
      {/* Toggle Button - Fixed position */}
      <button
        onClick={toggleSidebar}
        className="fixed left-4 top-4 z-50 flex h-10 w-10 items-center justify-center rounded-lg bg-zinc-900 text-white shadow-lg transition-all hover:bg-zinc-700 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-300"
        aria-label="Toggle sidebar"
      >
        {isOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
      </button>

      {/* Overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 z-30 bg-black/50 backdrop-blur-sm"
          onClick={toggleSidebar}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`fixed left-0 top-0 z-40 h-screen w-80 transform bg-white shadow-2xl transition-transform duration-300 ease-in-out dark:bg-zinc-900 ${
          isOpen ? "translate-x-0" : "-translate-x-full"
        }`}
      >
        <div className="flex h-full flex-col overflow-y-auto p-6">
          {/* Header */}
          <div className="mb-8 mt-12">
            <h2 className="text-2xl font-bold text-zinc-900 dark:text-zinc-100">
              Jasper Cantwell
            </h2>
            <p className="mt-1 text-sm text-zinc-600 dark:text-zinc-400">
              Full-Stack Software Engineer
            </p>
          </div>

          {/* Contact Information */}
          <div className="mb-8">
            <h3 className="mb-3 text-sm font-semibold uppercase tracking-wider text-zinc-500 dark:text-zinc-400">
              Contact
            </h3>
            <div className="space-y-3">
              <a
                href="tel:+447423781157"
                className="flex items-center gap-3 rounded-lg p-2 text-sm text-zinc-700 transition-colors hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-800"
              >
                <Phone className="h-4 w-4 text-zinc-500 dark:text-zinc-400" />
                <span>+44 7423 781157</span>
              </a>
              <a
                href="mailto:jasper66018@gmail.com"
                className="flex items-center gap-3 rounded-lg p-2 text-sm text-zinc-700 transition-colors hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-800"
              >
                <Mail className="h-4 w-4 text-zinc-500 dark:text-zinc-400" />
                <span className="break-all">jasper66018@gmail.com</span>
              </a>
            </div>
          </div>

          {/* Projects */}
          <div className="mb-8 flex-1">
            <h3 className="mb-3 text-sm font-semibold uppercase tracking-wider text-zinc-500 dark:text-zinc-400">
              Projects
            </h3>
            <div className="space-y-2">
              {projects.map((project) => (
                <div key={project.name} className="group relative">
                  <div className="flex items-start gap-3 rounded-lg p-3 transition-colors hover:bg-zinc-100 dark:hover:bg-zinc-800">
                    <Folder className="mt-0.5 h-4 w-4 shrink-0 text-zinc-500 dark:text-zinc-400" />
                    <div className="min-w-0 flex-1">
                      <p className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
                        {project.displayName}
                      </p>
                      <p className="mt-0.5 text-xs text-zinc-600 dark:text-zinc-400">
                        {project.description}
                      </p>
                    </div>
                  </div>

                  {/* Hover Tooltip with Links */}
                  <div className="pointer-events-none absolute -right-2 top-0 z-50 translate-x-full opacity-0 transition-all group-hover:pointer-events-auto group-hover:opacity-100">
                    <div className="ml-2 w-48 rounded-lg border border-zinc-200 bg-white p-3 shadow-xl dark:border-zinc-700 dark:bg-zinc-800">
                      <p className="mb-2 text-xs font-semibold text-zinc-900 dark:text-zinc-100">
                        {project.displayName}
                      </p>
                      <div className="space-y-2">
                        {project.websiteUrl && (
                          <a
                            href={project.websiteUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-center gap-2 rounded p-2 text-xs text-zinc-700 transition-colors hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-700"
                          >
                            <ExternalLink className="h-3 w-3" />
                            <span>Visit Website</span>
                          </a>
                        )}
                        {project.githubUrl && (
                          <a
                            href={project.githubUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="flex items-center gap-2 rounded p-2 text-xs text-zinc-700 transition-colors hover:bg-zinc-100 dark:text-zinc-300 dark:hover:bg-zinc-700"
                          >
                            <Github className="h-3 w-3" />
                            <span>View on GitHub</span>
                          </a>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* CV Download */}
          <div className="border-t border-zinc-200 pt-6 dark:border-zinc-800">
            <a
              href="/assets/Jasper_Cantwell_CV.pdf"
              download="Jasper_Cantwell_CV.pdf"
              className="flex items-center justify-center gap-2 rounded-lg bg-zinc-900 px-4 py-3 text-sm font-medium text-white transition-all hover:bg-zinc-700 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-300"
            >
              <Download className="h-4 w-4" />
              <span>Download CV</span>
            </a>
          </div>
        </div>
      </aside>
    </>
  );
}
