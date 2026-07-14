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
                "product_name": "Gaming Laptop",
                "price": 55000.00,
                "stock_quantity": 10,
                "created_at": datetime.now(),
                "discounted": True
            },
            {
                "product_name": "Wireless Mouse",
                "price": 799.00,
                "stock_quantity": 50,
                "created_at": datetime.now(),
                "discounted": False
            },
            {
                "product_name": "Mechanical Keyboard",
                "price": 3500.00,
                "stock_quantity": 15,
                "created_at": datetime.now(),
                "discounted": True
            },
            {
                "product_name": "USB-C Hub",
                "price": 2200.00,
                "stock_quantity": 30,
                "created_at": datetime.now(),
                "discounted": False
            },
            {
                "product_name": "Noise Cancelling Headphones",
                "price": 7500.00,
                "stock_quantity": 25,
                "created_at": datetime.now(),
                "discounted": True
            }
        ]
        result = collection.insert_many(products)
        print(f"\nInserted {len(result.inserted_ids)} documents successfully.\n")
        print(f"Document IDs: {result.inserted_ids}")

except Exception as e:
   print(f"Error during insert operation: {e}")


finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")
