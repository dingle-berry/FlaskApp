#!/usr/local/bin/python3

from flask import Flask, request, url_for, render_template
from markupsafe import escape
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/print_something_test/")
def print_something_test():
    print("THIS IS A TEST")
    return ("nothing")

@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login VIA POST"
    else:
        return "Login VIA GET"

@app.route("/hello/")
def hello():
    return ("Hello!!")

@app.route("/user/<username>")
def show_user_profile(username):
    return "User %s" % escape(username)

if __name__ == "__main__":
    app.run()
