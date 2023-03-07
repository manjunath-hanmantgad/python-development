from fastapi import APIRouter , Path
from model import test_1
test_router = APIRouter()


# creating in app database 

test_list = []

@test_router.post("/test_1")
async def add_test_1(test_1:dict):
    """ add a test_1 to test_list via POST method """
    test_list.append(test_1)
    return {"message": "Test_1 added successfully"}

@test_router.get("/test_1")

async def retrieve_test_1():
    """ retreive a test_1 to test_list via GET method """
    return {"test_1":"test_list"}

# next step is to serve to production.

# using Include_router() class as fastapi doesnt acccept
# router() class.


# this is for validating using pydantic.

test_list = []

@test_router.post("/test_1")
async def add_test_1(test_1:test_1): # got this from model.py 
    test_list.append(test_1)
    return {"message": "Test_1  added successfully - 2"}

@test_router.get("/test_1")
async def retrieve_test_1():
    
    return {"test_items": test_list}


@test_router.get("/test_1/{test_1_id}") # test_1_id is PATH parameter
async def get_single_record(test_1_id: int = Path(..., title="The ID to retrieve")):
    for t in test_list:
        if test_1.id == test_1_id:
            return{
                   "test_1": "test_1"
                   }
    return {
        "message": "Id with supplied item does not exist."
    }
