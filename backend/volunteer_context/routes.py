from fastapi import APIRouter

from volunteer_context.domain import Volunteer
from volunteer_context.volunteer_repository import create_volunteer

volunteer_context = APIRouter(prefix='/api/volunteer')

@volunteer_context.post("/register")
async def register(volunteer : Volunteer, id : str):
    try:
        id = await create_volunteer(volunteer, id)
        return {"id" : id}
    except Exception as e:
        print(e)
