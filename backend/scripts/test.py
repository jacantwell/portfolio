import requests

# Replace with your SSE endpoint URL
url = "http://127.0.0.1:8000/chat/stream"

# Headers are often needed for SSE
headers = {'Accept': 'text/event-stream'}
body = {
  "message": "can you tell me what languages Jasper's project s3-mobile uses",
  "temperature": 0.7
}

try:
    with requests.post(url, json=body, stream=True, headers=headers) as response:
        response.raise_for_status()
        
        print("Connected to SSE stream... Reading line by line.")
        
        # iter_lines() iterates over each line of the response
        for line in response.iter_lines():
            if line:
                # Decode the line (it's in bytes)
                decoded_line = line.decode('utf-8')
                
                # SSE data lines typically start with "data: "
                if decoded_line.startswith('data:'):
                    # Extract the data part (stripping "data: " and any whitespace)
                    data_str = decoded_line[len('data:'):].strip()
                    
                    if data_str == "[DONE]":
                        print("\nStream finished.")
                        break
                        
                    if data_str:
                          print(data_str, end="", flush=True) 

except requests.exceptions.RequestException as e:
    print(f"Stream connection error: {e}")