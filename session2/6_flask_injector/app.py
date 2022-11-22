from flask import Flask
from flask_injector import FlaskInjector 
from injector import inject, Binder
from flask import  request
import json

app = Flask(__name__)

class ItemsProvider(object):
    def __init__(self, items: list=[]):
        self._items = items
        
    def get(self, number_of_items: int=5) -> list:
        if not self._items:
            return []
        
        if number_of_items > len(self._items):
            number_of_items = len(self._items)
            
        return self._items[0:number_of_items]


@inject
@app.route("/user/")
def get_user(data_provider: ItemsProvider) -> list:
    return data_provider.get()

def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}])
    )
 

FlaskInjector(app=app, modules=[configure])

app.run()
