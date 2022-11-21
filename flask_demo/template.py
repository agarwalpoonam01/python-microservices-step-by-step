from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/greeting')
@app.route('/greeting/<name>')
def hello(name=None):
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run()

