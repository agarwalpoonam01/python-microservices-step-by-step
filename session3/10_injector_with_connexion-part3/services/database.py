import mysql.connector
import json

class MySqlDatabase(object):
    def __init__(self):
        self.db = mysql.connector.connect(host='127.0.0.1',database='user_info',user='root',password='root')
        self.cursor =  self.db.cursor(buffered=True)

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
        self.cursor.execute('INSERT INTO users(name,contact,email) VALUES ( %s, %s, %s)', (user['name'],user['contact'],user['email']))
        self.db.commit()
        return 'success'