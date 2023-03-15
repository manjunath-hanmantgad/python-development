'''
This file will handle routing operations such as creating, updating, and deleting events.
'''

# define the event router 

from fastapi import APIRouter,Body,HTTPException,status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)
events =[]

# define route to retrieve all events
# and event matching supplied ID in database


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=List[Event])
async def retrieve_event(id: int) -> Event:
    ''' raise 404 if an event with supplied id
    does not exist.'''
    for event in events:
        if event.id == id:
            return event 
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied id doesnt exist"

    )


# now implement thr routes to create event 

@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)

    return {
        "message":"Event created succesfully"
    }

@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message":"Event deleted"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="event with given id does not exists"
    )    

@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message":"events added succesfully"
    }