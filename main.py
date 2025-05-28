from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your OpenAI API Key (replace with your key or use env variable)
openai.api_key = "your-openai-api-key-here"  # TODO: Replace or use .env

@app.post("/ask-agent")
async def ask_agent(request: Request):
    data = await request.json()
    user_input = data.get("message")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful AI agent for business tasks."},
            {"role": "user", "content": user_input}
        ]
    )
    return {"reply": response.choices[0].message["content"]}
