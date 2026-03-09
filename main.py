# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()
MEMORY_FILE = "memory.json"

# Load memory if exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = []

class Prompt(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Hello, Anything-LLM!"}

@app.post("/chat")
def chat(prompt: Prompt):
    # Add user input to memory
    memory.append({"role": "user", "text": prompt.text})
    
    # Fake LLM response logic (you can improve this later)
    response_text = f"Anything-LLM reply to: '{prompt.text}'"
    
    memory.append({"role": "llm", "text": response_text})
    
    # Save memory to disk
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
    
    return {"response": response_text, "conversation": memory}
