from flask import render_template, redirect, url_for, flash
from user_story import app, db, bcrypt, login_manager
from user_story.forms import RegistrationForm, LoginForm, QuoteForm
from user_story.models import User, Quote
from flask_login import login_user, current_user, logout_user, login_required




@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    quotes = Quote.query.all()
    return render_template('home.html', title='Home', quotes=quotes)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, passwod=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Home', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.passwod, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Home', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


# New Quote Route
@app.route('/quote/new', methods=['GET', 'POST'])
def new_quote():
    form = QuoteForm()
    if form.validate_on_submit():
        quote = Quote(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(quote)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_quote.html', title='New Quote', legend='New Quote', form=form)