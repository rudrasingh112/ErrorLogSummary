import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
try:
    MONGO_URL = os.getenv("MONGO_DETAILS")
    print(" MongoDB configured successfully")
except ValueError:
    print("MongoDB failed to configure")

client= AsyncIOMotorClient(MONGO_URL)
database = client.log_analyzer
log_collection = database.get_collection("log_collection")