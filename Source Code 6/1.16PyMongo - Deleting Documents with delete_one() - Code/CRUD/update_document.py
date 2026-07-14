from connect_mongo import connect_to_mongodb

client = None

try:
   client = connect_to_mongodb()

   if client is not None:
       db = client['estore_pymongo']
       collection = db['products']
       update_query = collection.update_many(
           {"price": {"$lt": 3500}},
           {"$set": {"discounted": False}}
       )
       print(f"Matched: {update_query.matched_count} document(s)")
       print(f"Modified: {update_query.modified_count} document(s)")

except Exception as e:
 print(f"Error during insert operation: {e}")

finally:
 if client is not None:
     client.close()
     print("\nMongoDB connection closed.")
