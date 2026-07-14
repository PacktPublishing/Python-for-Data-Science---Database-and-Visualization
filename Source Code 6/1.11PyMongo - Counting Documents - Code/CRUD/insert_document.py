from connect_mongo import connect_to_mongodb
from datetime import datetime

client = None

try:
    client = connect_to_mongodb()

    if client is not None:
        db = client['estore_pymongo']
        collection = db['products']

        products = [
            {
                "product_name": "Mechanical Keyboard",
                "price": 3500.00,
                "stock_quantity": 15,
                "created_at": datetime.now()
            },
            {
                "product_name": "USB-C Hub",
                "price": 2200.00,
                "stock_quantity": 30,
                "created_at": datetime.now()
            },
            {
                "product_name": "Noise Cancelling Headphones",
                "price": 7999.00,
                "stock_quantity": 8,
                "created_at": datetime.now()
            }
        ]
        result = collection.insert_many(products, ordered=False)
        print(f"\nInserted {len(result.inserted_ids)} documents successfully.\n")
        print(f"Document IDs: {result.inserted_ids}")

except Exception as e:
   print(f"Error during insert operation: {e}")


finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")
