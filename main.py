from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="AI Interview Assistant",
    version="1.0"
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Models
# -----------------------------
class ChatRequest(BaseModel):
    message: str


class EvaluateRequest(BaseModel):
    answer: str


class FeedbackRequest(BaseModel):
    feedback: str


# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Interview Assistant 🚀"
    }


# -----------------------------
# Chat
# -----------------------------
@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are an AI Interview Assistant.
Answer interview questions clearly.
Keep answers professional and easy to understand.
"""
            },
            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    return {
        "message": response.choices[0].message.content
    }


# -----------------------------
# HR Questions
# -----------------------------
@app.get("/hr-questions")
def hr_questions():

    return {
        "questions": [
            "Tell me about yourself.",
            "Why should we hire you?",
            "What are your strengths?",
            "What are your weaknesses?",
            "Why do you want to join our company?",
            "Where do you see yourself in 5 years?",
            "Describe a challenge you faced.",
            "How do you handle pressure?",
            "What motivates you?",
            "Do you have any questions for us?"
        ]
    }


# -----------------------------
# Technical Questions
# -----------------------------
@app.get("/technical-questions")
def technical_questions():

    return {
        "questions": [
            "What is Python?",
            "What is FastAPI?",
            "What is an API?",
            "Difference between GET and POST?",
            "Difference between List and Tuple?",
            "What is OOP?",
            "What is JSON?",
            "What is SQL?",
            "Explain REST API.",
            "What is a Database?"
        ]
    }


# -----------------------------
# Evaluate
# -----------------------------
@app.post("/evaluate")
def evaluate(request: EvaluateRequest):

    prompt = f"""
Evaluate this interview answer.

Answer:
{request.answer}

Return:

Score /10

Strengths

Weaknesses

Suggestions
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "evaluation": response.choices[0].message.content
    }


# -----------------------------
# Feedback
# -----------------------------
@app.post("/feedback")
def feedback(request: FeedbackRequest):

    return {
        "message": "Thank you for your feedback! 😊",
        "feedback": request.feedback
    }