# coding:utf-8

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return '<h1>Hello, Knowledge Graph!</h1>'