from services.myservice import MyService
from flask_injector import inject

@inject
def get_data(ms: MyService):   
    return ms.get_data()
