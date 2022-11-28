import redis, time
from flask import request
from services.database import MySqlDatabase
from dotenv import load_dotenv
import os



class MyRedisDB(object):
    def __init__(self):
        load_dotenv()
        REDIS_DATABASE_HOST = os.getenv('REDIS_DATABASE_HOST')
        REDIS_DB_PORT = os.getenv('REDIS_DB_PORT')
        self.rdb = redis.StrictRedis(host=REDIS_DATABASE_HOST, port=REDIS_DB_PORT)
        
    def connect(self):
        # TODO: implementation for a MySQL database connection
        print("Successfully connected to Redis database!")

    def get_single_user(self, userid):
        user = self.rdb.get(userid)
        return user

    def set_single_user(self, userid, mydata):
        self.rdb.set(userid, mydata)
        return True

    def get_users(self):
        user = {}
        users = []
        for key in self.rdb.scan_iter():
            #user.append(key,values)
            value = self.rdb.get(key)
            user = {key: value}
            users.append(user)
            #print(key)
        #user = self.rdb.keys
        return str(users)
        
    
