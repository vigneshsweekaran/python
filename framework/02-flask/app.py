from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to python flask framework'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/info')
def info():
    return {
        "Programming Language": "Python",
        "Framework": "Flask"
    }