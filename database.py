from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['galaxy_classification_db']
images_collection = db['images']
