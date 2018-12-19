# coding:utf-8


from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'secret string'


@app.route('/')
@app.route('/home')
@app.route('/home/')
@app.route('/index')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/contributors')
def contributors():
    return render_template('contributors.html')