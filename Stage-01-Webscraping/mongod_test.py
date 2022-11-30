import pymongo

from pymongo import MongoClient

client = MongoClient('mongodb+srv://jpresto:sx67Lw3PFxJ9zkAw@cluster0.ot7fte8.mongodb.net/test')
db = client['test_database']


import datetime

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts

#post_id = posts.insert_one(post).inserted_id
#print(post_id)


