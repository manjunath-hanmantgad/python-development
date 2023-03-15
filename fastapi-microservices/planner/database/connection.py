from sqlmodel import JSON,SQLModel,Field,Column
from typing import Optional,List

class Event(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    # build a sublcass

    class Config:
        arbitary_types_allowed = True
        schema_extra = {
            "example": {
            "title": "Some event",
            "image": "https://stackoverflow.com/questions/2778840/socket-error-errno-10013-an-attempt-was-made-to-access-a-socket-in-a-way-forb/75729310#75729310",
            "description": "some description",
            "tags":["python","fastapi","database"],
            "location": "github"
            }
        }

        