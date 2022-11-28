
from flask import Flask
from flask_injector import FlaskInjector, inject
import connexion
from injector import singleton
from services.database import MySqlDatabase
from services.user import MyService
from connexion.resolver import RestyResolver
from services.redisdatabase import MyRedisDB

def configure(binder):
    binder.bind(MySqlDatabase, to=MySqlDatabase, scope=singleton)
    binder.bind(MyService, to=MyService, scope=singleton)
    binder.bind(MyRedisDB, to=MyRedisDB, scope=singleton)

if __name__ == '__main__':
    app = connexion.App(__name__, port=8080, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()
#, resolver=RestyResolver('api')