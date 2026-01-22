from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch", 
                "image": "https://i.pinimg.com/736x/2a/54/c7/2a54c75d16c89689016610afcd1fdd15.jpg",
                "description": "we will be discussing the contents of the FastAPI book in this event. ensure to come with your own copy ti win gifts!",
                "tags": ["python", "fastapi", "book", "launch"], 
                "location": "google meet"

            }
        }