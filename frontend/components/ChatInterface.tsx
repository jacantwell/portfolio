"use client";

import { useState, useRef, useEffect } from "react";
import { ArrowUp } from "lucide-react";

interface Message {
  id: string;
  content: string;
  role: "user" | "assistant";
  timestamp: Date;
}

export function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "1",
      content: "Hello! I'm Claude. How can I help you today?",
      role: "assistant",
      timestamp: new Date(),
    },
  ]);
  const [input, setInput] = useState("");
  const scrollRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

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

  const handleSend = () => {
    if (!input.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      content: input,
      role: "user",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    // Simulate AI response (placeholder for future backend integration)
    setTimeout(() => {
      const assistantMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: "This is a placeholder response. Backend integration coming soon!",
        role: "assistant",
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, assistantMessage]);
    }, 1000);
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

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
                    {message.role === "assistant" ? "C" : "U"}
                  </span>
                </div>
                <span className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
                  {message.role === "assistant" ? "Claude" : "You"}
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
      <div className="border-t border-zinc-200 bg-white dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mx-auto max-w-3xl px-4 py-6">
          <div className="relative flex items-end gap-2 rounded-2xl border border-zinc-300 bg-white px-4 py-3 shadow-sm focus-within:border-zinc-400 dark:border-zinc-700 dark:bg-zinc-800 dark:focus-within:border-zinc-600">
            <textarea
              ref={textareaRef}
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyPress}
              placeholder="Reply to Claude..."
              rows={1}
              className="max-h-[200px] flex-1 resize-none bg-transparent text-[15px] text-zinc-900 placeholder-zinc-400 outline-none dark:text-zinc-100 dark:placeholder-zinc-500"
            />
            <button
              onClick={handleSend}
              disabled={!input.trim()}
              className="flex h-8 w-8 shrink-0 items-center justify-center rounded-lg bg-zinc-900 text-white transition-all hover:bg-zinc-700 disabled:bg-zinc-200 disabled:text-zinc-400 dark:bg-zinc-100 dark:text-zinc-900 dark:hover:bg-zinc-300 dark:disabled:bg-zinc-700 dark:disabled:text-zinc-600"
            >
              <ArrowUp className="h-5 w-5" />
            </button>
          </div>
          <p className="mt-3 text-center text-xs text-zinc-500 dark:text-zinc-400">
            Claude can make mistakes. Please double-check responses.
          </p>
        </div>
      </div>
    </div>
  );
}
