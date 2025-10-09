from fastapi import FastAPI
import requests
import os

app = FastAPI()

OLLAMA_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.post("/generate")
def generate(prompt: str):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "llama3.2", "prompt": prompt},
        stream=False,
    )
    return response.json()
