from services.user import MyService
from flask_injector import inject

@inject
def get_users(ms: MyService):   
    return ms.get_users()

@inject
def store_user(ms: MyService, user):   
    return ms.store_user(user)

@inject
def get_single_user(ms: MyService, userid):
    return ms.get_single_user(userid)