from uuid import uuid4

from pydantic import BaseModel
from pydantic.main import BaseModel


class Charity(BaseModel):
    name : str
    charity_id : str
    description : str
    verified : bool

class CharityInDb(Charity):
    credentials_id : str
