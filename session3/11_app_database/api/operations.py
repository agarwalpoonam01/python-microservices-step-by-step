from services.user import MyService
from flask_injector import inject

@inject
def get_data(ms: MyService):   
    return ms.get_data()

@inject
def store_user(ms: MyService, user):   
    return ms.store_user(user)
