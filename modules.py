# Importing needed modules
from pydantic import BaseModel

# Data model for incoming quotes
class Quote(BaseModel):
    text: str
