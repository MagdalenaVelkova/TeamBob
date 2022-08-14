# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://admin:SkwDdH5v6M3DZ$p@cluster0.gvlkuqz.mongodb.net/?retryWrites=true&w=majority")
database = client.InterviewMasterDB

