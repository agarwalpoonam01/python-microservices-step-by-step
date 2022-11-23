from flask_injector import inject
from services.database import MySqlDatabase
from services.redisdatabase import MyRedisDB
import json

class MyService:
    @inject
    def __init__(self, dbase: MySqlDatabase, redisdb: MyRedisDB):
        print(f"DatabaseBase instance is {dbase.db}")  # We want to see the object that gets created
        self.dbase = dbase
        self.redisdb = redisdb
        self.dbase.db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY,name varchar(50), contact varchar(50), email varchar(50))')
    
    def get_users(self):
        return str(self.redisdb.get_users())

    def store_user(self,user):
        result = self.dbase.store_user(user)
        self.redisdb.set_single_user(user['id'], "name:  " + user['name'] + ",contact:  "+ user['contact'] + ",email:  " +  user['email'])
        return result

    def get_single_user(self, userid):
        result = self.redisdb.get_single_user(userid)
        print(result)
        str_result = str(result)
        if str_result != None:
            return str_result 
        else:
            user = self.dbase.get_single_user(userid)
            dict_user = json.dumps(user)
            if dict_user != None:
                mydata = "name: "+ dict_user[1] + ",contact:  " +  dict_user[2]+ ",email:  " + dict_user[3]
                print(dict_user[0], mydata)
                self.redisdb.set_single_user(dict_user[0], mydata)
                return dict_user
