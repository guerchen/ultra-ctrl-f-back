from datetime import datetime
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from bson.objectid import ObjectId
from app.mongo import collection

app = FastAPI()

class PageData(BaseModel):
    url: str
    images: List[str]
    timestamp: datetime

@app.post("/")
async def save_images(pageData: PageData):
    new_site_data = await collection.insert_one(jsonable_encoder(pageData))
    created_document = await collection.find_one({"_id": new_site_data.inserted_id})
    created_document["_id"] = str(created_document["_id"])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_document)