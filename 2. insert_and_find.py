from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.test_database
collection = db.test_collection

make_doc = {"name": "Alice", "age": 30, "city": "New York"}
inserted_id = collection.insert_one(make_doc).inserted_id
print(f"Inserted document with ID: {inserted_id}")

find_result = collection.find_one({"name": "Alice"})
if find_result:
    print("Found document:", find_result)
else:
    print("No document found with the specified criteria.")
    
find_result = collection.find_one({"name": "John"})
if find_result:
    print("Found document:", find_result)
else:
    print("No document found with the specified criteria.")