from flask import render_template, redirect, url_for
from user_story.forms import RegistrationForm, LoginForm, QuoteForm
from user_story.models import User, Quote
from user_story import app, db


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('register.html', title='Home', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', title='Home', form=form)


# New Quote Route
@app.route('/quote/new', methods=['GET', 'POST'])
def new_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(category=form.category.data, content=form.content.data)
        db.session.add(quote)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_quote.html', title='New Quote', legend='New Quote', form=form)