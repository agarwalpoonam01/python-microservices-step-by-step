import mysql.connector
import json
import redis
from flask import Flask
from flask import request
  
app = Flask(__name__)

db = mysql.connector.connect(host='127.0.0.1',database='user_info',user='demouser',password='demouser')
db.cursor().execute('CREATE TABLE IF NOT EXISTS users (id int PRIMARY KEY,name varchar(50), contact varchar(50), email varchar(50))')
cursor =  db.cursor(buffered=True)
rdb = redis.StrictRedis(host='redis-10317.c264.ap-south-1-1.ec2.cloud.redislabs.com', port=10317,
password='')

@app.route("/get_all")
def get():
    # Get all userinfo from redis cache
    user = {}
    users = []
    for key in rdb.scan_iter():
        value = rdb.get(key)
        user = {key: value}
        users.append(user)
    return str(users)

@app.route("/store", methods=["POST"])
def store_user():
    # store user info in db as well as in chache
    user = request.get_json()
    cursor.execute('INSERT INTO users(id,name,contact,email) VALUES (%s, %s, %s, %s)', (user['id'],user['name'],user['contact'],user['email']))
    db.commit()
    mydata = "name: "+ user["name"] + ",contact:  " + user['contact']+ ",email:  " + user['email']
    rdb.set(user['id'], mydata)
    return 'success'

@app.route("/get_user/<userid>")
def get_single_user(userid):
    #get from cache and if not present get from db and update cache
    result = rdb.get(userid)
    print("getting from cache")
    print(result)
    str_result = str(result)
    if result != None:
        return str_result 
    else:
        print("getting from db and updating cache")
        user = cursor.execute('SELECT * FROM users where id = %s', (userid,))
        users = cursor.fetchall()
        
        dict_user = json.dumps(users)
        if dict_user != None:
            mydata = "name: "+ dict_user[1] + ",contact:  " +  dict_user[2]+ ",email:  " + dict_user[3]
            print("redis_cache")
            print(dict_user)
            #print(dict_user[0], mydata)
            rdb.set(userid, mydata)
            #redisdb.set_single_user(dict_user[0], mydata)
            return dict_user

        return "user doesnot exist"

if __name__ == '__main__':
    app.run()
