from uuid import uuid4

from pydantic import BaseModel
from pydantic.main import BaseModel

# class CharityPreferences(BaseModel):

class Charity(BaseModel):
    name : str
    charity_id : str
    description : str
    verified : bool
    # to add preferences field of type CharityPreferences that captures all from the form

class CharityInDb(Charity):
    credentials_id : str
