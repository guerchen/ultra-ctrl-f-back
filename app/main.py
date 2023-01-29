from lib2to3.pytree import Base
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List
from app.mongo import db

app = FastAPI()

class PageData(BaseModel):
    url: str
    images: List[str]

@app.post("/")
async def save_images(pageData: PageData):
    new_site_data = await db.site_images.insert_one(jsonable_encoder(pageData))
    created_document = await db.site_images.find_one({"_id": str(new_site_data.inserted_id)})
    print(created_document)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_document)