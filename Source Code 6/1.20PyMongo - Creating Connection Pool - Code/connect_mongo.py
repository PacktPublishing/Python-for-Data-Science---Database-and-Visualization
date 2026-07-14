from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_to_mongodb():
    try:
        client = MongoClient(
            host="mongodb://localhost:27017/",
            maxPoolSize=30,
            minPoolSize=10,
            maxIdleTimeMS=30000,
            waitQueueTimeoutMS=5000
        )
        client.admin.command('ping')
        print("MongoDB pool connected.\n")
        return client

    except ConnectionFailure as e:
        print(f"Error while connecting to MongoDB: {e}")
        return None

if __name__ == "__main__":
    my_client = connect_to_mongodb()
    if my_client:
        print("Connection pool configured successfully!")
        my_client.close()
        print("\nMongoDB connection closed.")
