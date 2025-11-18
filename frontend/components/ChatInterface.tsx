"use client";

import { useState, useRef, useEffect } from "react";
import { ArrowUp, Menu } from "lucide-react";
import { Button } from "@/components/retroui/Button";
import { Textarea } from "./retroui/Textarea";
import { Badge } from "./retroui/Badge";
import ReactMarkdown from "react-markdown";
import { Loader } from "@/components/retroui/Loader";

const TEXT_DISPLAY_DELAY = 30; // Delay in ms for text display

interface Message {
  id: string;
  content: string;
  role: "user" | "assistant";
  timestamp: Date;
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

interface ChatInterfaceProps {
  toggleSidebar: () => void;
}

export function ChatInterface({ toggleSidebar }: ChatInterfaceProps) {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "1",
      content: "Hello! I'm Jasper. How can I help you today?",
      role: "assistant",
      timestamp: new Date(),
    },
  ]);
  const [input, setInput] = useState("");
  const [isStreaming, setIsStreaming] = useState(false);
  const [isWaitingForResponse, setIsWaitingForResponse] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  useEffect(() => {
    if (textareaRef.current) {
      // Reset height to auto to get the correct scrollHeight
      textareaRef.current.style.height = "auto";

      // Calculate new height with a maximum limit
      const maxHeight = 150; // Maximum height in pixels (approximately 5-6 lines)
      const newHeight = Math.min(textareaRef.current.scrollHeight, maxHeight);

      textareaRef.current.style.height = newHeight + "px";

      // Enable overflow scrolling if content exceeds max height
      textareaRef.current.style.overflowY =
        textareaRef.current.scrollHeight > maxHeight ? "auto" : "hidden";
    }
  }, [input]);

  const streamResponse = async (messageContent: string) => {
    // Create assistant message placeholder
    const assistantMessageId = (Date.now() + 1).toString();
    const assistantMessage: Message = {
      id: assistantMessageId,
      content: "",
      role: "assistant",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, assistantMessage]);
    setIsWaitingForResponse(true);

    try {
      // Create abort controller for this request
      abortControllerRef.current = new AbortController();

      const response = await fetch(`${API_URL}/chat/stream`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "text/event-stream",
        },
        body: JSON.stringify({ message: messageContent }),
        signal: abortControllerRef.current.signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const reader = response.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) {
        throw new Error("Failed to get response reader");
      }

      let buffer = "";
      let textQueue = ""; // Queue for text to be displayed
      let isDisplaying = false;
      let firstChunkReceived = false;

      // Function to display queued text with delay
      const displayQueuedText = async () => {
        if (isDisplaying) return;
        isDisplaying = true;

        while (textQueue.length > 0) {
          // Take 1-3 characters at a time for a natural feel
          const chunkSize = Math.min(
            Math.floor(Math.random() * 3) + 1,
            textQueue.length
          );
          const chunk = textQueue.slice(0, chunkSize);
          textQueue = textQueue.slice(chunkSize);

          setMessages((prev) =>
            prev.map((msg) =>
              msg.id === assistantMessageId
                ? { ...msg, content: msg.content + chunk }
                : msg
            )
          );

          await new Promise((resolve) =>
            setTimeout(resolve, TEXT_DISPLAY_DELAY)
          );
        }

        isDisplaying = false;
      };

      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          // Make sure all queued text is displayed before finishing
          while (textQueue.length > 0) {
            await new Promise((resolve) => setTimeout(resolve, 10));
          }
          break;
        }

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";

        for (const line of lines) {
          if (line.startsWith("data:")) {
            const data = line.slice(5).trim();
            if (data) {
              // Turn off waiting state when first chunk arrives
              if (!firstChunkReceived) {
                setIsWaitingForResponse(false);
                firstChunkReceived = true;
              }
              // Add to queue instead of displaying immediately
              textQueue += data;
              displayQueuedText(); // Start displaying if not already
            }
          }
        }
      }
    } catch (error: unknown) {
      if (error instanceof Error && error.name === "AbortError") {
        console.log("Request aborted");
      } else {
        console.error("Error streaming response:", error);
        setMessages((prev) =>
          prev.map((msg) =>
            msg.id === assistantMessageId
              ? {
                  ...msg,
                  content:
                    msg.content ||
                    "Sorry, I encountered an error. Please try again.",
                }
              : msg
          )
        );
      }
    } finally {
      setIsStreaming(false);
      setIsWaitingForResponse(false);
      abortControllerRef.current = null;
    }
  };

  const handleSend = async () => {
    if (!input.trim() || isStreaming || isWaitingForResponse) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      content: input,
      role: "user",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    const userInput = input;
    setInput("");
    setIsStreaming(true);

    await streamResponse(userInput);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleSuggestedMessage = async (message: string) => {
    if (isStreaming || isWaitingForResponse) return;

    setInput(message);
    // Small delay to show the input before sending
    await new Promise((resolve) => setTimeout(resolve, 100));

    const userMessage: Message = {
      id: Date.now().toString(),
      content: message,
      role: "user",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsStreaming(true);

    await streamResponse(message);
  };

  const suggestedMessages = [
    "Walk me through your tech stack",
    "Have you worked with cloud platforms?",
    "Can you tell me about Jasper's s3-mobile project",
  ];

  const hasUserMessage = messages.some((m) => m.role === "user");

  return (
    <div className="flex h-screen flex-col bg-white dark:bg-zinc-900">
      {/* Messages Area */}
      <div ref={scrollRef} className="flex-1 overflow-y-auto">
        <div className="mx-auto max-w-3xl px-4 py-8">
          {messages.map((message) => (
            <div
              key={message.id}
              className={`mb-8 ${
                message.role === "user" ? "ml-auto max-w-2xl" : ""
              }`}
            >
              <div className="mb-2 flex items-center gap-2">
                {message.role === "assistant" ? (
                  <Badge variant="surface" className="h-full outline-0">
                    Jasper
                  </Badge>
                ) : (
                  <Badge variant="solid" className="h-full outline-0">
                    You
                  </Badge>
                )}
              </div>
              <div className="pl-8">
                <ReactMarkdown>{message.content}</ReactMarkdown>
              </div>
            </div>
          ))}

          {/* Loading indicator */}
          {isWaitingForResponse && (
            <div className="pl-8">
              <Loader />
            </div>
          )}
        </div>
      </div>

      {/* Input Area */}
      <div className={hasUserMessage ? "" : "py-5"}>
        <div className="mx-auto max-w-3xl px-4 py-2">
          {/* Suggested Messages */}
          {!hasUserMessage && (
            <div className="mb-4 flex flex-col gap-2 px-4">
              {suggestedMessages.map((message, index) => (
                <Button
                  variant="outline"
                  key={index}
                  onClick={() => handleSuggestedMessage(message)}
                >
                  {message}
                </Button>
              ))}
            </div>
          )}

          <div className="relative flex items-center gap-2 px-4 py-2">
            <Button
              size="icon"
              onClick={toggleSidebar}
              variant="secondary"
              className="flex-shrink-0"
            >
              <Menu className="w-6 h-6" />
            </Button>
            <Textarea
              ref={textareaRef}
              value={input}
              onChange={(e: React.ChangeEvent<HTMLTextAreaElement>) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Ask me a question..."
              rows={1}
              className="px-4 py-2 w-full border-2 shadow-md transition focus:outline-hidden focus:shadow-xs"
            />
            <Button
              size="icon"
              onClick={handleSend}
              disabled={!input.trim() || isStreaming || isWaitingForResponse}
              className=""
            >
              <ArrowUp className="w-6 h-6" />
            </Button>
          </div>
          <p className="mt-3 text-center text-xs text-zinc-500 dark:text-zinc-400">
            Jasper can make mistakes. Please double-check responses.
          </p>
        </div>
      </div>
    </div>
  );
}
