
from main import database

from volunteer_context.domain import Volunteer, VolunteerInDb

Volunteers = database.Volunteers

async def create_volunteer(volunteer : Volunteer, id):
    entity = VolunteerInDb(credentials_id = id, first_name = volunteer.first_name,last_name = volunteer.last_name, eligability = volunteer.eligability, hair_length = volunteer.hair_length,donation_timeframe = volunteer.donation_timeframe )
    result = await Volunteers.insert_one(entity.dict())
    if result.acknowledged == True:
        return {"credentials_id" : id}
    else:
        raise Exception ("Something went wrong but developer was too lazy so log it") 
