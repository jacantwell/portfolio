"use client";

import { useState, useRef, useEffect } from "react";
import { ArrowUp } from "lucide-react";

interface Message {
  id: string;
  content: string;
  role: "user" | "assistant";
  timestamp: Date;
}

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export function ChatInterface() {
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
      textareaRef.current.style.height = "auto";
      textareaRef.current.style.height = textareaRef.current.scrollHeight + "px";
    }
  }, [input]);

  const handleSend = async () => {
    if (!input.trim() || isStreaming) return;

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

    // Create assistant message placeholder
    const assistantMessageId = (Date.now() + 1).toString();
    const assistantMessage: Message = {
      id: assistantMessageId,
      content: "",
      role: "assistant",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, assistantMessage]);

    try {
      // Create abort controller for this request
      abortControllerRef.current = new AbortController();

      const response = await fetch(`${API_URL}/chat/stream`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "text/event-stream",
        },
        body: JSON.stringify({ message: userInput }),
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
      let wordBuffer = ""; // Buffer to accumulate characters for word-by-word display
      let displayedContent = ""; // Track what's been displayed

      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          // Flush any remaining word buffer at the end
          if (wordBuffer) {
            displayedContent += wordBuffer;
            setMessages((prev) =>
              prev.map((msg) =>
                msg.id === assistantMessageId
                  ? { ...msg, content: displayedContent }
                  : msg
              )
            );
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
              // Add incoming data to word buffer
              wordBuffer += data;

              // Check if we have complete words to display
              // Split on spaces, but keep track of incomplete words
              const lastSpaceIndex = wordBuffer.lastIndexOf(" ");
              const lastNewlineIndex = wordBuffer.lastIndexOf("\n");
              const lastBreakIndex = Math.max(lastSpaceIndex, lastNewlineIndex);

              if (lastBreakIndex !== -1) {
                // We have at least one complete word
                const completeText = wordBuffer.substring(0, lastBreakIndex + 1);
                displayedContent += completeText;
                wordBuffer = wordBuffer.substring(lastBreakIndex + 1);

                // Update the message with complete words
                setMessages((prev) =>
                  prev.map((msg) =>
                    msg.id === assistantMessageId
                      ? { ...msg, content: displayedContent }
                      : msg
                  )
                );
              }
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
      abortControllerRef.current = null;
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleSuggestedMessage = async (message: string) => {
    if (isStreaming) return;

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

    // Create assistant message placeholder
    const assistantMessageId = (Date.now() + 1).toString();
    const assistantMessage: Message = {
      id: assistantMessageId,
      content: "",
      role: "assistant",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, assistantMessage]);

    try {
      abortControllerRef.current = new AbortController();

      const response = await fetch(`${API_URL}/chat/stream`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "text/event-stream",
        },
        body: JSON.stringify({ message }),
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
      let wordBuffer = ""; // Buffer to accumulate characters for word-by-word display
      let displayedContent = ""; // Track what's been displayed

      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          // Flush any remaining word buffer at the end
          if (wordBuffer) {
            displayedContent += wordBuffer;
            setMessages((prev) =>
              prev.map((msg) =>
                msg.id === assistantMessageId
                  ? { ...msg, content: displayedContent }
                  : msg
              )
            );
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
              // Add incoming data to word buffer
              wordBuffer += data;

              // Check if we have complete words to display
              // Split on spaces, but keep track of incomplete words
              const lastSpaceIndex = wordBuffer.lastIndexOf(" ");
              const lastNewlineIndex = wordBuffer.lastIndexOf("\n");
              const lastBreakIndex = Math.max(lastSpaceIndex, lastNewlineIndex);

              if (lastBreakIndex !== -1) {
                // We have at least one complete word
                const completeText = wordBuffer.substring(0, lastBreakIndex + 1);
                displayedContent += completeText;
                wordBuffer = wordBuffer.substring(lastBreakIndex + 1);

                // Update the message with complete words
                setMessages((prev) =>
                  prev.map((msg) =>
                    msg.id === assistantMessageId
                      ? { ...msg, content: displayedContent }
                      : msg
                  )
                );
              }
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
      abortControllerRef.current = null;
    }
  };

  const suggestedMessages = [
    "Walk me through your tech stack",
    "Have you worked with cloud platforms?",
    "Show me React projects",
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
                <div
                  className={`flex h-6 w-6 items-center justify-center rounded ${
                    message.role === "assistant"
                      ? "bg-amber-600 text-white"
                      : "bg-zinc-200 dark:bg-zinc-700"
                  }`}
                >
                  <span className="text-xs font-semibold">
                    {message.role === "assistant" ? "J" : "U"}
                  </span>
                </div>
                <span className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
                  {message.role === "assistant" ? "Jasper" : "You"}
                </span>
              </div>
              <div className="pl-8">
                <p className="whitespace-pre-wrap text-[15px] leading-relaxed text-zinc-900 dark:text-zinc-100">
                  {message.content}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Input Area */}
      <div className={hasUserMessage ? "" : "py-15"}>
        <div className="mx-auto max-w-3xl px-4 py-6">
          {/* Suggested Messages */}
          {!hasUserMessage && (
            <div className="mb-4 flex flex-col gap-2">
              {suggestedMessages.map((message, index) => (
                <button
                  key={index}
                  onClick={() => handleSuggestedMessage(message)}
                  className="rounded-lg border border-zinc-300 bg-white px-4 py-3 text-left text-sm text-zinc-700 transition-all hover:border-zinc-400 hover:bg-zinc-50 dark:border-zinc-700 dark:bg-zinc-800 dark:text-zinc-300 dark:hover:border-zinc-600 dark:hover:bg-zinc-700"
                >
                  {message}
                </button>
              ))}
            </div>
          )}

          <div className="relative flex items-center gap-2 rounded-2xl border border-zinc-300 bg-white px-4 py-2 shadow-sm focus-within:border-zinc-400 dark:border-zinc-700 dark:bg-zinc-800 dark:focus-within:border-zinc-600">
            <textarea
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Ask Jasper a question..."
              rows={1}
              className="max-h-[200px] flex-1 resize-none bg-transparent text-[15px] text-zinc-900 placeholder-zinc-400 outline-none dark:text-zinc-100 dark:placeholder-zinc-500"
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || isStreaming}
              className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-zinc-900 text-white transition-all hover:bg-zinc-700 disabled:bg-zinc-200 disabled:text-zinc-400 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-300 dark:disabled:bg-zinc-700 dark:disabled:text-zinc-600"
            >
              <ArrowUp className="h-5 w-5" />
            </button>
          </div>
          {/* <p className="mt-3 text-center text-xs text-zinc-500 dark:text-zinc-400">
            Jasper can make mistakes. Please double-check responses.
          </p> */}
        </div>
      </div>
    </div>
  );
}
