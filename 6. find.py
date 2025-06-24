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
    
    fruit = collection.find_one({"name": "apples"})
    print("Exact Match Query Result:", fruit)
    
    fruits = collection.find({"color": "yellow"})
    print("Documents with color yellow:")
    for doc in fruits:
        print(doc)
        
    all_fruits = collection.find()
    print("All documents in the collection:")
    for doc in all_fruits:
        print(doc)
        
    # Sorting documents
    asc_sorted_fruits = collection.find({"color": "yellow"}).sort("qty", ASCENDING)
    print("Fruits sorted by quantity in ascending order:")
    for doc in asc_sorted_fruits:
        print(doc)    
        
    desc_sorted_fruits = collection.find({"color": "yellow"}).sort("qty", DESCENDING)
    print("Fruits sorted by quantity in descending order:")
    for doc in desc_sorted_fruits:
        print(doc)    
except Exception as e:
    print("An error occurred:", e)
finally:
    client.close()
    print("Connection closed.")