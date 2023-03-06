from fastapi import FastAPI , APIRouter
app = FastAPI() # initialize the fastapi 
from test_1 import test_router
'''
@app decorator contains 8 methods:
get(), post(), delete(), put(), head(), patch(), trace(), and options()

'''

# creating routes 

@app.get("/")
async def welcome():
    return {"message": "Hello there!"}

# what if there are multiple routes
# using APIRouter()

'''
The APIRouter class belongs to the FastAPI package and creates path operations for multiple routes.
'''
router = APIRouter()
@router.get("/hello")
async def say_hello():
    return {"message":"hello!"}



