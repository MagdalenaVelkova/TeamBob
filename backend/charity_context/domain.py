from uuid import uuid4

from pydantic import BaseModel
from pydantic.main import BaseModel


class Charity(BaseModel):
    id: str = uuid4().hex
    name : str
    charity_id : str
    description : str
    verified : bool

