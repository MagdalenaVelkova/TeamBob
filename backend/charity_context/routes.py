
from fastapi import APIRouter

from charity_context.charity_context_repository import create_charity
from charity_context.domain import Charity

charity_context = APIRouter(prefix='/api/charity')


@charity_context.post("/register")
async def register(charity : Charity, id : str):
    try:
        id = await create_charity(charity, id)
        return {"id" : id}
    except Exception as e:
        print(e)
