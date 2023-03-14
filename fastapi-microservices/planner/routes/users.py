'''
This file will handle routing operations such as the registration and signing-in of users.
'''

# defining user routes 

from fastapi import APIRouter,HTTPException,status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

users = {}

@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with given username already exists"
        )
    users[data.email] = data # add user data into the users.
    return {
        "message": "User succesfully registerd"
    }

# now for checking if email exists 

@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    if users[user.email] not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="USer not exists"
        )
    if users[user.email].password !=user.password:
        raise HTTPException(
            status_code=status.HTTP_404_FORBIDDEN,
            detail="Wrong credentials"
        )
    return{
        "message":"User signed in succefully"
    }

'''
1. Check user exists in database , if not exist then exception is raised.
2. IF user exist then application wull check if password is matching.
'''