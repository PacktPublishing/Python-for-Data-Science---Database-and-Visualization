from connect_mongo import connect_to_mongodb
from pprint import pprint

client = None

try:
   client = connect_to_mongodb()
   if client is not None:
       db = client['estore_pymongo']
       collection = db['products']

       products = collection.find(
           {"price": {"$gt": 799}},
           {"product_name": 1, "price": 1,
            "stock_quantity": 1, "_id": 0}
       )
       for product in products:
           pprint(product, sort_dicts=False, width=100)

except Exception as e:
  print(f"Error during insert operation: {e}")

finally:
  if client is not None:
      client.close()
      print("\nMongoDB connection closed.")
