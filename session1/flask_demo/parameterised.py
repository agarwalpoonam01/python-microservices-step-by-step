
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello you are in the home page"

@app.route("/<name>")
def user(name):
    return f"Home {name}"

if __name__ == '__main__':
    app.run()

