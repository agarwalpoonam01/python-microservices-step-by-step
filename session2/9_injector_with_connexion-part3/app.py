import sqlite3
import connexion
from injector import Binder
from flask_injector import FlaskInjector 
from connexion.resolver import RestyResolver
from services.users import Users
from injector import singleton


def configure(binder: Binder) -> Binder:
    binder.bind(
        sqlite3.Connection,
        to=sqlite3.Connection(':memory:', check_same_thread=False),
        scope=singleton,
    )


if __name__ == '__main__':
    app = connexion.App(__name__, port=8080, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run()