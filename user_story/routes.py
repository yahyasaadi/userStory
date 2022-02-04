from flask import render_template, redirect, url_for
from user_story.forms import RegistrationForm, LoginForm
from user_story import app


stories = [
    {
        'author': 'Yahya Saadi',
        'title': 'Pickup line',
        'content': 'Well here I am. What are your other two wishes'
    },
    {
        'author': 'Home',
        'title': 'Pickup line',
        'content': "Hey, my name's Microsoft. Can I crash at your place tonight?"
    },
    {
        'author': 'Stewie',
        'title': 'Pickup line',
        'content': "Are you French? Because Eiffel for you."
    }
]





@app.route('/')
def home():
    return render_template('home.html', title='Home', stories=stories)


@app.route('/register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title='Home', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', title='Home', form=form)