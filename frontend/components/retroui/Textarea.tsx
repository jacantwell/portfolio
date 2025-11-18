import React from "react";
import { cn } from "@/lib/utils";

export const Textarea = React.forwardRef<
  HTMLTextAreaElement,
  React.TextareaHTMLAttributes<HTMLTextAreaElement>
>(({ placeholder = "Enter text...", className = "", ...props }, ref) => {
  return (
    <textarea
      ref={ref}
      placeholder={placeholder}
      rows={4}
      className={cn(
        "px-4 py-2 w-full border-2 rounded border-border shadow-md transition focus:outline-hidden focus:shadow-xs placeholder:text-muted-foreground resize-none",
        className
      )}
      {...props}
    />
  );
});

Textarea.displayName = "Textarea";
