from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import get_gemini_response  # Import the chatbot function

# Initialize the FastAPI application
app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request body structure using Pydantic
class ChatRequest(BaseModel):
    input_text: str

# Create an endpoint for the chatbot
@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    try:
        # Call the chatbot function and get the response
        response = get_gemini_response(request.input_text)
        return {"response": response}
    except Exception as e:
        # Handle exceptions and errors
        raise HTTPException(status_code=500, detail=str(e))


