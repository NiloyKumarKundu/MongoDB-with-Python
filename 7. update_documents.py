from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient("localhost", 27017)

try:
    database = client["sample_fruit"]
    collection = database["fruits"]

    # collection.insert_many([
    #     { "_id": 1, "name": "apples", "qty": 5, "rating": 3, "color": "red", "type": ["fuji", "honeycrisp"] },
    #     { "_id": 2, "name": "bananas", "qty": 7, "rating": 4, "color": "yellow", "type": ["cavendish"] },
    #     { "_id": 3, "name": "oranges", "qty": 6, "rating": 2, "type": ["naval", "mandarin"] },
    #     { "_id": 4, "name": "pineapple", "qty": 3, "rating": 5, "color": "yellow" },
    # ])
    
    # Update a single document
    result = collection.update_one({"name": "apples"}, {"$set": {"name": "green apples"}})
    print(f"Matched {result.matched_count} document(s) and modified {result.modified_count} document(s).")
    
    print("Updated document:")
    updated_fruit = collection.find()
    for doc in updated_fruit:
        print(doc)
        
    
    # Update multiple documents
    query_filter = {"color": "yellow"}
    update_operation = {"$set": {"color": "golden yellow", "qty": 10}}
    result = collection.update_many(query_filter, update_operation)
    
    print("Updated multiple documents:")
    updated_fruit = collection.find()
    for dec in updated_fruit:
        print(dec)
except Exception as e:
    print("An error occurred:", e)
finally:
    client.close()
    print("Connection closed.")