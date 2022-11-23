import mysql.connector
import json


class MySqlDatabase(object):
    def __init__(self):
        self.db = mysql.connector.connect(host='127.0.0.1',database='user_info',user='demouser',password='demouser')
        self.cursor =  self.db.cursor(buffered=True)
       # self.redidb = redis.Redis('localhost')
    def connect(self):
        # TODO: implementation for a MySQL database connection
        print("Successfully connected to MySQL database!")

    def get(self):
        #self.cursor = db.cursor(buffered=True)
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()
        print(users)
        return json.dumps(users)
    
    def store_user(self, user):

        self.cursor.execute('INSERT INTO users(id,name,contact,email) VALUES (%s, %s, %s, %s)', (user['id'],user['name'],user['contact'],user['email']))
        self.db.commit()
        return 'success'

    def get_single_user(self, userid):
        #self.cursor = db.cursor(buffered=True)
        
        self.cursor.execute('SELECT * FROM users where id = %s', (userid,))
        users = self.cursor.fetchall()
        print(users)
        return json.dumps(users)