import mysql.connector
import json
from dotenv import load_dotenv
import os


class MySqlDatabase(object):
    def __init__(self):
        load_dotenv()
        MYSQL_HOST = os.getenv('MYSQL_HOST')
        MYSQL_USER = os.getenv('MYSQL_USER')
        MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
        MYSQL_DATABASE_NAME = os.getenv('MYSQL_DATABASE_NAME')
        self.db = mysql.connector.connect(host=MYSQL_HOST,database=MYSQL_DATABASE_NAME,user=MYSQL_USER,password=MYSQL_PASSWORD)
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