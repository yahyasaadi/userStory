from flask import Flask, render_template

app = Flask(__name__)


from user_story import routes

