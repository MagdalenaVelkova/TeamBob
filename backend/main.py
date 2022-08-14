import ssl

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#app object
app = FastAPI()


app.add_middleware(
CORSMiddleware,
allow_origins=['*'],
allow_credentials = True,
allow_methods=["*"],
allow_headers=["*"]
)
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:SkwDdH5v6M3DZ$p@cluster0.gvlkuqz.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE", connect=False)
db = client.test


database = client.HairDonator



from charity_context.routes import charity_context
# import routes
from user_context.routes import user_context
from volunteer_context.routes import volunteer_context

# add routes to app 
app.include_router(user_context)
app.include_router(charity_context)
app.include_router(volunteer_context)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
