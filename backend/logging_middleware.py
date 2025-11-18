import time
import json
import logging
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Message

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to log all incoming requests and outgoing responses.
    Captures method, path, headers, body, status code, and response time.
    """
    
    async def set_body(self, request: Request):
        """Capture and store request body"""
        receive_ = await request._receive()
        
        async def receive() -> Message:
            return receive_
        
        request._receive = receive
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Start timer
        start_time = time.time()
        
        # Capture request details
        request_id = request.headers.get("x-request-id", f"{time.time()}")
        
        # Get request body if present
        request_body = None
        if request.method in ["POST", "PUT", "PATCH"]:
            try:
                body = await request.body()
                if body:
                    request_body = body.decode('utf-8')
                    # Try to parse as JSON for better logging
                    try:
                        request_body = json.loads(request_body)
                    except json.JSONDecodeError:
                        pass
            except Exception as e:
                logger.warning(f"Could not read request body: {e}")
        
        # Log request
        request_log = {
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "query_params": dict(request.query_params),
            "client_host": request.client.host if request.client else None,
            "user_agent": request.headers.get("user-agent"),
            "content_type": request.headers.get("content-type"),
        }
        
        if request_body:
            request_log["body"] = request_body
        
        logger.info(f"REQUEST: {json.dumps(request_log)}")
        
        # Process request
        try:
            response = await call_next(request)
        except Exception as e:
            # Log error
            process_time = time.time() - start_time
            error_log = {
                "request_id": request_id,
                "error": str(e),
                "process_time": f"{process_time:.3f}s"
            }
            logger.error(f"ERROR: {json.dumps(error_log)}")
            raise
        
        # Calculate process time
        process_time = time.time() - start_time
        
        # Log response
        response_log = {
            "request_id": request_id,
            "status_code": response.status_code,
            "process_time": f"{process_time:.3f}s",
        }
        
        logger.info(f"RESPONSE: {json.dumps(response_log)}")
        
        # Add custom header with process time
        response.headers["X-Process-Time"] = str(process_time)
        
        return response