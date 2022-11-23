import redis, time
from flask import request
from services.database import MySqlDatabase

class MyRedisDB(object):
    def __init__(self):
        self.rdb = redis.StrictRedis(host='redis-10317.c264.ap-south-1-1.ec2.cloud.redislabs.com', port=10317,
  password='')
        
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
        
    
