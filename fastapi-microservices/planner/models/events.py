'''
This file will handle routing operations such as creating, updating, and deleting events.
'''

# define the event 

from pydantic import BaseModel
from typing import List 

class Event(BaseModel):
    id: int
    title:str 
    image: str
    description: str
    tags: List[str]
    location: str

    # creating a subclass
    # config subclass : shows what model data will look

    class Config:
        schema_extra= {
            "example": {
            "title": "My fast api program",
            "image": "https://unsplash.com/photos/KBMfW-Mkfhs",
            "description": "Describes what program I write.",
            "tags":["python","fastapi","photography"],
            "location":"Github"
            
            }
        }
