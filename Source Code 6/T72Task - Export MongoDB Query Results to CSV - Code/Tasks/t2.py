from connect_mongo import connect_to_mongodb
import csv

client = None

try:
   client = connect_to_mongodb()
   if client is not None:
       db = client['estore_pymongo']
       collection = db['products']
       query = collection.find(
           {},
           {
               "_id": 0,
               "product_name": 1,
               "price": 1,
               "stock_quantity": 1,
           }).sort("price", -1).limit(5)
       # print("Top 5 most expensive products:")
       # print("-" * 50)
       # for product in query:
       #     print(product)

       filename = "mongodb_products.csv"
       with open(filename, mode='w', newline='', encoding='utf-8') as file:
           writer = csv.writer(file)
           writer.writerow(['Product Name', 'Price', 'Stock'])
           for product in query:
               print(product)
               writer.writerow([
                   product['product_name'],
                   product['price'],
                   product['stock_quantity']
               ])
           print(f"\nData exported successfully to '{filename}'")

except Exception as e:
 print(f"Error during insert operation: {e}")

finally:
 if client is not None:
     client.close()
     print("\nMongoDB connection closed.")
