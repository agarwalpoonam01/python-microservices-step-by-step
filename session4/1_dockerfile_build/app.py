import sqlite3
from flask import Flask, Config
from flask.views import View
from flask_injector import FlaskInjector 
from injector import inject, singleton
from flask import  request
import json

app = Flask(__name__)

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

@inject
@app.route("/user/")
def get_users(u: Users):   
    return u.get_users()

@inject
@app.route("/user/<name>", methods=['POST'])
def add_user(u: Users,name):   
    return u.add_user(name)


def configure(binder):
    binder.bind(
        sqlite3.Connection,
        to=sqlite3.Connection(':memory:', check_same_thread=False),
        scope=singleton,
    )

FlaskInjector(app=app, modules=[configure])

app.run(host='0.0.0.0', port=5000)
