from fastapi import FastAPI
from routes.users import user_router
import uvicorn

# creating fastapi instance and register route and application 

app = FastAPI()

# route registeration 

app.include_router(user_router, prefix="/user")
# include the event 
app.include_router(event_router, prefix="/event")
if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", 
                #port=8080,
                port=8000,
                reload=True)