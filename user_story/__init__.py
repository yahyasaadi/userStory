from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f1c65efed6134c1bc305ffa153496th0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pass_root@localhost/userstory'
db = SQLAlchemy(app)


from user_story import routes

