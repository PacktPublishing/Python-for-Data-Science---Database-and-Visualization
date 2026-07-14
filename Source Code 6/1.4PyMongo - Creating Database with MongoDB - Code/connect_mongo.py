from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


client = None


try:
   client = MongoClient("mongodb://localhost:27017/")
   print("Connected to MongoDB.\n")
   db = client['estore_pymongo']
   print(db.name)


except ConnectionFailure as e:
   print("Error while connecting to MongoDB:", e)


finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")

