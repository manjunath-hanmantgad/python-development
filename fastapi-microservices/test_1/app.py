from fastapi import FastAPI

from test_1 import test_router
#from model import test_1
app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World"
    }


app.include_router(test_router)