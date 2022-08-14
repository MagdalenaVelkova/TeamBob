import enum
from typing import Optional

from pydantic import BaseModel
from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class UserTypeEnum(str, enum.Enum):
    CHARITY = "charity"
    VOLUNTEER = "volunteer"

class User(BaseModel):
    email : EmailStr
    type: UserTypeEnum

class UserInDB(User):
    hashed_password: str

class UserInRegister(User):
    password: str
        
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


