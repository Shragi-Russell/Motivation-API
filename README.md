# Motivational Quotes API

## Description
A simple FastAPI project to manage motivational quotes. 

## Features
- View a random quote
- View all quotes
- Add a new quote
- Update an existing quote
- Delete a quote

## How to Run
1. Install dependencies: pip install fastapi uvicorn
2. Run the server: uvicorn main:app --reload
3. Open in your browser: http://127.0.0.1:8000


## Endpoints
- `GET /` - Welcome message
- `GET /quote` - Get a random quote
- `GET /quotes` - Get all quotes
- `POST /quote` - Add a new quote (JSON: `{"text": "Your quote"}`)
- `DELETE /quote` - Delete a quote (JSON: `{"text": "Quote to delete"}`)
- `PUT /quote` - Update a quote (JSON: `{"old_quote": {"text": "Old quote"}, "new_quote": {"text": "New quote"}}`)
