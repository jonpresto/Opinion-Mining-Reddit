import praw
import pymongo
from pymongo import MongoClient
import json

# MongoDB connection string
client = MongoClient('mongodb+srv://jpresto:sx67Lw3PFxJ9zkAw@cluster0.ot7fte8.mongodb.net/test')


# Reddit credentials
with open('credentials.txt', 'r') as f:
    credentials_data = f.read()
credentials = json.loads(credentials_data)


# Accessing the reddit api
reddit = praw.Reddit(
    client_id = credentials['client_id'],
    client_secret = credentials['client_secret'],
    username = credentials['username'],
    password = credentials['password'],
    user_agent = credentials['user_agent']
)

# Access a subreddit
subreddit_name = 'spotify'

# Print submission titles for the top 10 hottest posts right now
for submission in reddit.subreddit(subreddit_name).hot(limit=10):
    print(submission.title)


# Test connection to a MongoDB collection from Python
from pymongo import MongoClient

# Create a method to connect to a MongoDB collection
def connect_mongo(database_name, collection_name):
    """
    Input:
    - database_name (string): name of the database
    - collection_name (string): name of the collection

    Output:
    - collection (MongoDB collection)
    """
    username = credentials['username']
    password = credentials['password']
    database = database_name
    mongo_url = 'mongodb+srv://jpresto:sx67Lw3PFxJ9zkAw@cluster0.ot7fte8.mongodb.net/test'
    client = MongoClient(mongo_url)
    db = client[database_name]
    collections = db[collection_name]
    return collections

# connect to db instance and fetch 10 records
mycollection = connect_mongo("sample_geospatial", "shipwrecks")
records = mycollection.find().limit(10)
for doc in records:
    #Print each document
    print(doc)

# connect to db instance and fetch 5 records using filters
mycollection = connect_mongo("sample_geospatial", "shipwrecks")
records = mycollection.find({'feature_type': 'Wrecks - Visible'}).limit(5)

for doc in records:
    #Print each document
    print(doc)


# connect to db instance, insert a record, then output updated collection list
mycollection = connect_mongo("test_database", "posts")

'''
import datetime
post = {"author": "Chris",
        "text": "My third blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
        
mycollection.insert_one(post)
'''


records = mycollection.find().limit(10)
for doc in records:
    #Print each document
    print(doc)