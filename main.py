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

 Defining endpoint for random quote
@app.get("/quote")
async def get_quote():
    # Select a random quote from the list
    quote = random.choice(quotes)
    return {"quote": quote}

# Defining endpoint for all quotes
@app.get("/quotes")
async def get_all_quotes():
    return {"quotes": quotes}
