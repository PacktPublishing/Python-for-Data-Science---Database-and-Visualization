from connect_mongo import connect_to_mongodb
from bson import ObjectId

client = None

try:
   client = connect_to_mongodb()
   if client is not None:
       db = client['estore_pymongo']
       collection = db['products']
       product_id = ObjectId("696093cda39927a254715487")
       update_query = collection.update_one(
           {"_id": product_id},
           {"$set": {
               "price": 7500,
               "stock_quantity": 25,
               "on_sale": True
           }}
       )
       print(f"Matched: {update_query.matched_count},"
             f"Modified: {update_query.modified_count}")

       print("Updated Document:")
       product = collection.find_one({"_id": product_id})
       print(product)

except Exception as e:
 print(f"Error during insert operation: {e}")

finally:
 if client is not None:
     client.close()
     print("\nMongoDB connection closed.")
