from connect_mongo import connect_to_mongodb

client = None

try:
  client = connect_to_mongodb()
  if client is not None:
      db = client['estore_pymongo']
      query = client.drop_database('estore_pymongo')
      print("Database removed successfully.")

except Exception as e:
   print(f"Error during insert operation: {e}")

finally:
   if client is not None:
       client.close()
       print("\nMongoDB connection closed.")
