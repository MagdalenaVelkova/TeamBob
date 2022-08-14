from datetime import datetime
from typing import Dict
from uuid import uuid4

from pydantic import BaseModel, Field


class TimePeriod(Dict):
    start : datetime
    end : datetime

class Volunteer(BaseModel):
    first_name : str
    last_name : str
    eligability : bool
    hair_length : int
    donation_timeframe : TimePeriod

class VolunteerInDb(Volunteer):
    credentials_id : str
