# coding:utf-8


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return '<h1>Hello, Knowledge Graph!</h1>'

'''
Search
Introduction
Contributors
'''
@app.route('/search')
def search():
    return render_template('base.html')