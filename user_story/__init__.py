import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from user_story.config import Config

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'f1c65efed6134c1bc305ffa153496th0'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:pass_root@localhost/userstory'
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from user_story import routes

