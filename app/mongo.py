import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb+srv://admin:x0FZl46PiWffq4eV@ultra-ctrl-f.ecday84.mongodb.net/?retryWrites=true&w=majority"
    )

db = client.site_images

print(db.SiteImages.find_one())

