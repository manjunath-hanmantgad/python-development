from fastapi import APIRouter , Path
test_router = APIRouter()


# creating in app database 

test_list = []

@test_router.post("/test_1")
async def add_test_1(test_1:dict):
    test_list.append(test_1)
    return {"message": "Test_1 added successfully"}

@test_router.get("/test_1")

async def retrieve_test_1():
    return {"test_1":"test_list"}
