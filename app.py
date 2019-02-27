from flask import Flask

app = Flask(__name__)


@app.route('/')
def show():
    print("Confusia says: Man with watch has time on side")
