# Importing needed modules
from fastapi import FastAPI
from models import Quote
from quotes import quotes
import random

# Creating a FastAPI app instance
app = FastAPI()

# Middleware to add X-Content-Type-Options header
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response

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

# Defining endpoint to add a new quote
@app.post("/quote")
async def add_quote(new_quote: Quote):
    # Checking if teh quote already exits in the list
    if new_quote.text in quotes:
        return {"message": "Quote already exists."}
    quotes.append(new_quote.text)
    return {"message": "Quote added successfully!"}

# Defining endpoint to delete a quote
@app.delete("/quote")
async def delete_quote(quote: Quote):
    if quote.text in quotes:
        quotes.remove(quote.text)
        return {"message": "Quote deleted successfully!"}
    return {"message": "Quote not found."}

 Defining endpoint to update a quote
@app.put("/quote")
async def update_quote(old_quote: Quote, new_quote: Quote):
    if old_quote.text in quotes:
        index = quotes.index(old_quote.text)
        quotes[index] = new_quote.text
        return {"message": "Quote updated successfully!"}
    return {"message": "Quote not found."}
