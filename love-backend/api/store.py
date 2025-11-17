from fastapi import FastAPI
from fastapi import Request
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI()

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["love_calculator"]
collection = db["pairs"]

class Pair(BaseModel):
    name1: str
    name2: str
    percentage: int

@app.post("/api/store")
async def store_pair(pair: Pair):
    doc = {
        "name1": pair.name1,
        "name2": pair.name2,
        "percentage": pair.percentage
    }
    result = collection.insert_one(doc)

    return {
        "status": "success",
        "id": str(result.inserted_id)
    }

