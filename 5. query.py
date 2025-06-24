from pymongo import MongoClient

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
    
    # Exact match query
    query = {"name": "apples"}
    find = collection.find_one(query)
    print("Exact Match Query Result:", find)
    
    # Comparison Operators
    query = {"qty": {"$gt": 5}}
    multiple_find = collection.find(query)
    print("Documents with qty > 5:")
    for doc in multiple_find:
        print(doc)

    # Logical Operators
    
    results = collection.find({ 
        "$or": [
            { "qty": { "$gt": 5 }},
            { "color": "yellow" },
            {"type": "cavendish" }
        ]
    })

    print("Documents with qty > 5 or color yellow or type cavendish:")
    for f in results:
        print(f)


    ## Array Operators
    results = collection.find({
        "type" : { "$size": 2 }
    })

    print("Documents with type array size of 2:")
    for f in results:
        print(f)
        
        
    results = collection.find({
        "type" : { "$size": 1 }
    })

    print("Documents with type array size of 1:")
    for f in results:
        print(f)
        
    results = collection.find({
        "type" : { "$all": ["cavendish"] }
    })

    print("Documents with type array all:")
    for f in results:
        print(f)
        
    results = collection.find({
        "type" : { "$elemMatch": {"$eq": "cavendish"} }
    })

    print("Documents with type array elemMatch:")
    for f in results:
        print(f)
        
    results = collection.find( { "color" : { "$exists": "true" }} )

    print("Documents with color field exists:")
    for f in results:
        print(f)
    
    results = collection.find({ "name" : { "$regex" : "p{2,}" }} )
    print("Documents with name field matching regex:")
    for f in results:
        print(f)
    
except Exception as e:
    raise Exception("Error inserting documents: ", e)

finally:
    if client:
        client.close()
        print("MongoDB connection closed.")