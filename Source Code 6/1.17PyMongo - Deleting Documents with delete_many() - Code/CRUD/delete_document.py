from connect_mongo import connect_to_mongodb

client = None

try:
  client = connect_to_mongodb()
  if client is not None:
      db = client['estore_pymongo']
      collection = db['products']
      query = collection.delete_many(
          {
              "discounted": True,
              "price": {"$lt": 4000}
          }
      )
      print(f"Deleted Count: {query.deleted_count}")

except Exception as e:
   print(f"Error during insert operation: {e}")

finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")
