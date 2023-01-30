from typing import Collection
import motor.motor_asyncio
import asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    ""
    )

db = client.site_images
collection = db.SiteImages