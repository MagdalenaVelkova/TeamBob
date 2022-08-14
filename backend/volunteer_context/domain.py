from datetime import datetime
from typing import Dict
from uuid import uuid4

from pydantic import BaseModel


class TimePeriod(Dict):
    start : datetime
    end : datetime

class Volunteer(BaseModel):
    first_name : str
    last_name : str
    eligability : bool
    hair_length : int
    donation_timeframe : TimePeriod
    show_to_charities: bool
    # preferences field that captures all from the form

class VolunteerInDb(Volunteer):
    credentials_id : str
