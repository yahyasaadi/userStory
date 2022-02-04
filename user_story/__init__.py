from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f1c65efed6134c1bc305ffa153496th0'


from user_story import routes

