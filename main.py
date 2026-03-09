# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Anything-LLM Minimal Server")

# Define a request schema
class PromptRequest(BaseModel):
    prompt: str

# Root endpoint to check server
@app.get("/")
def read_root():
    return {"message": "Hello, Anything-LLM!"}

# Mock endpoint to simulate a response from the model
@app.post("/generate")
def generate_text(request: PromptRequest):
    prompt = request.prompt
    # This is a mock response. Replace with real model logic later.
    generated_text = f"Echo: {prompt}"
    return {"prompt": prompt, "response": generated_text}
