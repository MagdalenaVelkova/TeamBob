from datetime import datetime, timedelta
from typing import List, Optional

from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWEError
from main import database
from passlib.context import CryptContext
from starlette import status

from user_context.domain import TokenData, UserInDB, UserInRegister

#UserProfilesDB = database.UserProfiles
UserDB = database.User

SECRET_KEY = "8f39cb20cb17bbda4a053f8d0cc2e7ba1344deeedc566b04"
ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(email: str):
    user = await UserDB.find_one({"email":email})
    if user:
        return user
    return False

async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWEError:
        raise credentials_exception
    user = await get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def create_user(user : UserInRegister):
    hashed_password = get_password_hash(user.password)

    new_user_credentials = UserInDB(email = user.email,type = user.type, hashed_password = hashed_password)
    #new user profile for the relevant type 
    result = await UserDB.insert_one(new_user_credentials.dict())
    #await UserProfilesDB.insert_one(new_user_profile.dict())
    return result



