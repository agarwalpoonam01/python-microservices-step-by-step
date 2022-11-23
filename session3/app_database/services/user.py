from flask_injector import inject
from services.database import MySqlDatabase
class MyService:
    @inject
    def __init__(self, dbase: MySqlDatabase):
        print(f"DatabaseBase instance is {dbase.db}")  # We want to see the object that gets created
        self.dbase = dbase
        self.dbase.db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY AUTO_INCREMENT,name varchar(50), contact varchar(50), email varchar(50))')
    
    def get_data(self):
        return self.dbase.get()

    def store_user(self,user):
        return self.dbase.store_user(user)