#!/usr/local/bin/python3

from flask import Flask, request, url_for, render_template, flash, redirect
from markupsafe import escape
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5e7767fa8e90916f723b0f57a249ac90b93ff412dbf19fd76e2c6b0265763e06'

posts = [
    {
        'author': 'Chance Boyd',
        'title': 'Post number 1',
        'content': 'First post content for testing',
        'date_posted': 'April 14, 2020'
    },
    {
        'author': 'Michellee Boyd',
        'title': 'Post number 2',
        'content': 'Second post content for testing',
        'date_posted': 'April 13, 2020'

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
