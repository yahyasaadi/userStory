import os

class Config:
    SECRET_KEY = os.environ.get('S_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SDU')