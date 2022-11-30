
import praw
import pymongo
from pymongo import MongoClient
import json

# MongoDB connection string
client = MongoClient('mongodb+srv://jpresto:sx67Lw3PFxJ9zkAw@cluster0.ot7fte8.mongodb.net/test')
#db = client['reddit_db']

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

# Create a method to connect to MongoDB collection
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


mycollection = connect_mongo("sample_geospatial", "shipwrecks")
record = mycollection.find_one()
print(record)