from flask_injector import inject

import json
import sqlite3

class Users(object):
    @inject
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self.db.execute('CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT ,name text NOT NULL)')

    def get_users(self):
        users = self.db.execute('SELECT * FROM users').fetchall()
        return json.dumps(users)
    
    def add_user(self,name):
        self.db.execute('INSERT INTO users(name) VALUES (?)', (name,))
        return 'success'