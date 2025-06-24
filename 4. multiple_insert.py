from typing import TypedDict
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

try:
    db = client.get_database("test_database")
    collection = db.get_collection("test_collection")
    
    document_lists = [
        {"name": "Rahim", "age": 25, "city": "Dhaka"},
        {"name": "Karim", "age": 28, "city": "Chittagong"},
        {"name": "Sultana", "age": 22, "city": "Sylhet"},
        {"name": "Fatema", "age": 30, "city": "Rajshahi"},
        {"name": "Hasan", "age": 35, "city": "Khulna"}
    ]
    result = collection.insert_many(document_lists)
    print(f"Inserted document IDs: {result.inserted_ids}")
    
    find = collection.find_one({"name": "Rahim"})
    if find:
        print("Found document:", find)
        
    multiple_find = collection.find({"age": 30})
    for doc in multiple_find:
        print("Found document with age 30:", doc)
        
    count = collection.count_documents({})

    print(count)
    
    count = collection.estimated_document_count()

    print(count)
    
    results = collection.distinct("name")

    for document in results:
        print(document)

    client.close()
except Exception as e:
    print("An error occurred:", e)
