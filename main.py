# Importing needed modules
from fastapi import FastAPI
from models import Quote
from quotes import quotes
import random

# Creating a FastAPI app instance
app = FastAPI()

# Defining the root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Motivational Quotes API!"}
