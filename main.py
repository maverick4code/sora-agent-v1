from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import os

app = FastAPI()

# Set up CORS for frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define Pydantic model for request body
class Message(BaseModel):
    message: str

@app.post("/ask-agent")
async def ask_agent(msg: Message):
    user_input = msg.message

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful AI agent."},
            {"role": "user", "content": user_input}
        ]
    )
    return {"reply": response.choices[0].message["content"]}
