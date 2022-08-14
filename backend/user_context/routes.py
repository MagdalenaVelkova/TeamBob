from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from user_context.domain import Token, User, UserInRegister
from user_context.user_repository import (authenticate_user,
                                          create_access_token, create_user,
                                          get_current_user)

user_context = APIRouter(prefix="/api/authentication")


ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Create token
@user_context.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):   
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

# View profile
@user_context.get("/user/myprofile/", response_model=User)
async def get_my_profile(current_user: User = Depends(get_current_user)):
    return current_user

# Register User
@user_context.post("/register")
async def register(user : UserInRegister):
    result = await create_user(user)
    return str(result)
