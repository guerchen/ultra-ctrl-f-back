import motor.motor_asyncio
from app.env import mongo 

client = motor.motor_asyncio.AsyncIOMotorClient(
    f"mongodb+srv://{mongo['username']}:{mongo['password']}@ultra-ctrl-f.ecday84.mongodb.net/?retryWrites=true&w=majority"
    )

db = client.site_images
collection = db.SiteImages

def daily_site_image_array():
    #TODO: Query DB to get all images saved to a specific domain
    pass