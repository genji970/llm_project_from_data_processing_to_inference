from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "ml_database"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]
collection = db["predictions"]