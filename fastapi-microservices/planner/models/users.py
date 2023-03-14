from pydantic import BaseModel, EmailStr
from typing import Optional, List
# importing the events from the /models/Event
from models.events import Event

class User(BaseModel):

    email: EmailStr

    password: str

    events: Optional[List[Event]]

    # define a subclass that indicates how user data is stored and set.

    class Config:
        schema_extra = {
            "example":{
            "email":"mj@gmail.com",
            "username":"beast-mode-on",
            "events":[],
            }
        }