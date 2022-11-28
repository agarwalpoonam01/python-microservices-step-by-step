import json
from flask import Flask
from flask import request
import pymongo
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
MONGO_DATABASE_HOST = os.getenv('MONGO_DATABASE_HOST')
MONGO_DB_PORT = os.getenv('MONGO_DB_PORT')
myclient = pymongo.MongoClient("mongodb://"+ MONGO_DATABASE_HOST + ":" + MONGO_DB_PORT +"/")

mydb = myclient["feedback-db"]
mycol = mydb["users"]


@app.route("/get-feedback/<user_email>")
def get(user_email):
    a = []
    myquery = { "email": user_email }
    for x in mycol.find(myquery,{ "_id": 0, "username": 1, "email": 1, "contact": 1, "feedback": 1 }):
        print(x)
        a.append(x)
    return a
    # Get all userinfo from mongodb


@app.route("/store-feedback", methods=["POST"])
def store_user():
    # store user info in db 
    user = request.get_json()
    mycol.insert_one(user)
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
