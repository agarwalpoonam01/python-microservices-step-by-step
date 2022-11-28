import time

import redis
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
REDIS_DATABASE_HOST = os.getenv('REDIS_DATABASE_HOST')
REDIS_DB_PORT = os.getenv('REDIS_DB_PORT')
app = Flask(__name__)
cache = redis.Redis(host=REDIS_DATABASE_HOST, port=REDIS_DB_PORT)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
