# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so you can access from your phone browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (phone, laptop)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data model for incoming prompts
class PromptRequest(BaseModel):
    prompt: str

# In-memory memory for storing conversation
memory = []

# Simple "simulated LLM response"
def fake_llm_response(prompt):
    # Here you can customize how responses look
    return f"LLM says: '{prompt[::-1]}'"  # just reverses the prompt as a dummy response

@app.get("/")
def read_root():
    return {"message": "Hello! Anything-LLM interactive environment is running."}

@app.post("/predict")
def predict(request: PromptRequest):
    response = fake_llm_response(request.prompt)
    memory.append({"prompt": request.prompt, "response": response})
    return {"response": response}

@app.get("/memory")
def get_memory():
    return {"memory": memory}
