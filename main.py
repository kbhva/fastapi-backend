from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_gemini_response  # Import the chatbot function

# Initialize the FastAPI application
app = FastAPI()

# Specify allowed origins for CORS
origins = [
    "http://localhost:3000",                  # Local development
    "https://firstcheque.vercel.app",         # Vercel-hosted website
    "https://firstcheque-chatbot.onrender.com" # Render-hosted backend
]

# Add CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,                    # Allow these domains
    allow_credentials=True,                   # Enable credentials
    allow_methods=["*"],                      # Allow all HTTP methods
    allow_headers=["*"],                      # Allow all HTTP headers
)

# Define the request body structure using Pydantic
class ChatRequest(BaseModel):
    input_text: str

# Create an endpoint for the chatbot
@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    try:
        print("Request received:", request.input_text)  # Debugging log
        # Call the chatbot function and get the response
        response = get_gemini_response(request.input_text)
        print("Generated response:", response)          # Debugging log
        return {"response": response}
    except Exception as e:
        print("Error processing request:", str(e))      # Debugging log
        # Handle exceptions and return error details
        raise HTTPException(status_code=500, detail=str(e))

# Start the FastAPI server when run directly
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))  # Default to port 8080 if PORT is not set
    print(f"Starting server on port {port}")            # Debugging log
    uvicorn.run(app, host="0.0.0.0", port=port)
