from datetime import datetime
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from bson.objectid import ObjectId
from app.mongo import collection
from app.preprocessing import preprocess
from app.model import find_similar
from pymongo import DESCENDING

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PageData(BaseModel):
    url: str
    images: List[str]
    timestamp: datetime

class CompareData(BaseModel):
    url: str
    reference_image: str

@app.post("/save")
async def save_images(pageData: PageData):
    new_site_data = await collection.insert_one(jsonable_encoder(pageData))
    created_document = await collection.find_one({"_id": new_site_data.inserted_id})
    created_document["_id"] = str(created_document["_id"])
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_document)

@app.post("/compare")
async def compare_images(compareData: CompareData):
    page_images = await collection.find({"url": compareData.url}).sort("timestamp", DESCENDING).to_list(1)
    preprocessed_images = preprocess(page_images[0]['images'])
    try:
        similar_index = find_similar(compareData.reference_image, preprocessed_images.drop(columns='url'))
        similar_images = preprocessed_images['url'].loc[similar_index].drop_duplicates().values
        return JSONResponse(status_code=200, content={"similar":list(similar_images)})
    except Exception as error:
        return JSONResponse(status_code=400, content={"error":str(error)})