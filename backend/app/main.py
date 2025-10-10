from fastapi import FastAPI, Form, Request
import requests
import os
import pymysql 


app = FastAPI()

OLLAMA_URL = os.getenv("OLLAMA_API_URL", "http://ollama:11434")

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

# @app.post("login")
# def login():
#     response =