from datetime import datetime
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from bson.objectid import ObjectId
from app.mongo import collection
from app.preprocessing import preprocess
from app.model import find_similar

app = FastAPI()

class PageData(BaseModel):
    url: str
    images: List[str]
    timestamp: datetime

class CompareData(BaseModel):
    url: str
    reference_image: str

@app.post("/")
async def save_images(pageData: PageData):
    new_site_data = await collection.insert_one(jsonable_encoder(pageData))
    created_document = await collection.find_one({"_id": new_site_data.inserted_id})
    created_document["_id"] = str(created_document["_id"])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_document)

@app.post("/compare")
async def compare_images(compareData: CompareData):
    page_images = await collection.find({"url": compareData.url})
    preprocessed_images = preprocess(page_images)
    similar_images = preprocessed_images.loc[find_similar(preprocessed_images.drop('url'))]
    return JSONResponse(status_code=200, content={list(similar_images['url'])})