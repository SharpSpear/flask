from flask import Flask, request, jsonify
from flask import render_template, request
from markupsafe import escape
# from flask_sqlalchemy import SQLAlchemy
# import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html', thing_to_say = 'hello_world')
@app.route('/login', methods=['POST', 'GET'])
def login_page():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)
    return 'login_page'

@app.route('/user/<name>')
def display_user(name):
    return 'User %s' % escape(name)
@app.route('/total/<int:amount>')
def display_total_amount(amount):
    print(amount)
@app.route('/path/<path:sub_path>')
def take_to_subpath(sub_path):
    print(sub_path)
@app.route('/key/<uuid:api_key>')
def display_key(api_key):
    print(api_key)

app.debug = True
if __name__ == '__main__':
   app.run()