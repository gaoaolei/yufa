# coding:utf-8
# default port of flask is 5000
# run in python2.7
from flask import Flask
from flask import request

app = Flask(__name__)  
print app 

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1><a href="http://localhost:5000/signin">Login</a>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    
    if request.form['username']=='gaoaolei' and request.form['password']=='4209841413pl':
        return '<h3>Hello, gaoaolei!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()