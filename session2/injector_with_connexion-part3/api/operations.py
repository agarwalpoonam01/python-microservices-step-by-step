from services.users import Users
from flask_injector import inject

@inject
def get_users(u: Users):   
    return u.get_users()

@inject
def add_user(u: Users,name):   
    return u.add_user(name)
