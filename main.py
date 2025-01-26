from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Define the request schema (optional, if you want a POST request)
class Message(BaseModel):
    msg: str

# GET endpoint: /text
@app.get("/text")
async def hello_world_get(msg: str = "Hello, World!"):
    """
    Handles GET requests at /text and returns the message.
    """
    return {"message": msg}

# POST endpoint: /text
@app.post("/text")
async def hello_world_post(data: Message):
    """
    Handles POST requests at /text and returns the message.
    """
    return {"message": data.msg}

