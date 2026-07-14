from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_to_mongodb():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        client.admin.command('ping')
        print("Connected to MongoDB.\n")
        return client

    except ConnectionFailure as e:
        print(f"Error while connecting to MongoDB: {e}")
        return None

if __name__ == "__main__":
    my_client = connect_to_mongodb()
    if my_client:
        my_client.close()
        print("\nMongoDB connection closed.")
