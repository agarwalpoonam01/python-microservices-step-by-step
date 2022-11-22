from flask_injector import inject
from services.database import MySqlDatabase
class MyService:
    @inject
    def __init__(self, db: MySqlDatabase):
        print(f"DatabaseBase instance is {db}")  # We want to see the object that gets created
        self.db = db

    def get_data(self):
        return self.db.get()