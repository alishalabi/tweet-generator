from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Confusia say: Man with watch has time on side'
