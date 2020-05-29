import pymongo
from pymongo import MongoClient


CONNECTION_STRING = "mongodb+srv://dbMyUniversity:TWEB2020myUniversityPWA@myuniversitymongodb-9xszi.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')

