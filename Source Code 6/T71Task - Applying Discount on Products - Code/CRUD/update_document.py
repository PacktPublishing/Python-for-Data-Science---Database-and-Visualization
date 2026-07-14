from connect_mongo import connect_to_mongodb

client = None

try:
   client = connect_to_mongodb()

   if client is not None:
       db = client['estore_pymongo']
       collection = db['products']
       products = collection.find(
           {
               "price": {"$gte": 3500},
               "discounted": True
           },
           {"price": 1}
       )
       for product in products:
           original_price = product["price"]
           discounted_price = original_price - (original_price * 0.15)

           collection.update_one(
                {"_id": product["_id"]},
                   {
                       "$set": {
                           "discount": 15,
                           "discounted_price": round(discounted_price, 2)
                       }
                   }
           )
       updated_products = collection.find(
           {"price": {"$gte": 3500}},
           {
               "product_name":1,
               "price":1,
               "discount":1,
               "discounted_price":1,
               "_id":0
            }
       )
       for product in updated_products:
           print(product)

except Exception as e:
 print(f"Error during insert operation: {e}")

finally:
 if client is not None:
     client.close()
     print("\nMongoDB connection closed.")
