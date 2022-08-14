from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel


class TimePeriod():
    start : datetime
    end : datetime

class Charity(BaseModel):
    id: str = uuid4().hex
    first_name : str
    last_name : str
    eligability : bool
    hair_length : float
    donation_timeframe : TimePeriod
