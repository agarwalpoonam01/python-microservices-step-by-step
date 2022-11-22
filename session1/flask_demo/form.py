from flask import Flask, request
app = Flask(__name__)
@app.route('/formtest', methods=['POST', 'GET'])
def form_test():
    if request.method == 'POST':
        return 'Username: %s' % (request.form['username'])
    else:
        return '''  <form action="/formtest" method="post">
            Name: <input name="username" type="text" /> <br/>
            <input value="Send" type="submit" />
        </form>  '''
if __name__ == "__main__":
    app.run()
