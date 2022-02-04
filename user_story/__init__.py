from flask import Flask, render_template

app = Flask(__name__)


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
    return render_template('home.html', stories=stories)

