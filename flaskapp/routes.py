from flask import request, url_for, render_template, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post

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

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # DEBUG: Fake login for testing
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed.  Bad username or password', 'danger')
            return render_template('login.html', title='Login', form=form)
    return render_template('login.html', title='Login', form=form)


