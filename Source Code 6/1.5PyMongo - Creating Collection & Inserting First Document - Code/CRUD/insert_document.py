from connect_mongo import connect_to_mongodb
from datetime import datetime

client = None

try:
    client = connect_to_mongodb()

    if client is not None:
        db = client['estore_pymongo']
        collection = db['products']

        product = {
            "product_name": "Wireless Mouse",
            "description": "Silent optical mouse with adjustable DPI.",
            "price_info": {
                "value": 799.00,
                "currency": "USD",
            },
            "stock_quantity": 50,
            "created_at": datetime.now()
        }
        result = collection.insert_one(product)
        print(f"Inserted document with ID: {result.inserted_id}")

except Exception as e:
   print(f"Error during insert operation: {e}")


finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")
