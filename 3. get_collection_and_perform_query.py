from pymongo import MongoClient

client = MongoClient("localhost", 27017)

try:
    db = client.get_database("test_database")
    collection = db.get_collection("test_collection")
    
    query = {"name": "Alice"}
    find = collection.find_one(query)
    
    print("Query Result:", find)
    
    client.close()
except Exception as e:
    print("An error occurred:", e)