from bson import ObjectId
from main import database

from charity_context.domain import Charity, CharityInDb

Charities = database.Charities
async def fetch_all_charities():
    return 0

async def create_charity(charity : Charity, id):
    entity = CharityInDb(credentials_id = id, name = charity.name,charity_id = charity.charity_id, description = charity.description, verified = charity.verified )
    result = await Charities.insert_one(entity.dict())
    if result.acknowledged == True:
        return {"credentials_id" : id}
    else:
        raise Exception ("Something went wrong but developer was too lazy so log it") 
