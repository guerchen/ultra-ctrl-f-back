import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://admin:x0FZl46PiWffq4eV@ultra-ctrl-f.ecday84.mongodb.net/?retryWrites=true&w=majority"
    )
db = client.site_images

print(db.SiteImages.find_one())

