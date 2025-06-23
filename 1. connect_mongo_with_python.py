from pymongo import MongoClient

# client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
client = MongoClient("localhost", 27017)

try:
    # Attempt to connect to the MongoDB server
    client.admin.command('ping')
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Failed to connect to MongoDB:", e)
