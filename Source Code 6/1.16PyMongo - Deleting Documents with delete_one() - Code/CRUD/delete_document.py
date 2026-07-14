from connect_mongo import connect_to_mongodb
from bson import ObjectId

client = None

try:
  client = connect_to_mongodb()
  if client is not None:
      db = client['estore_pymongo']
      collection = db['products']
      product_id = ObjectId("696093cda39927a254715486")
      query = collection.delete_one({"_id": product_id})
      print(f"Deleted Count: {query.deleted_count}")

except Exception as e:
   print(f"Error during insert operation: {e}")

finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")
