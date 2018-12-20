# coding:utf-8


from flask import Flask, render_template
from forms import SearchForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'secret string'

db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
@app.route('/home/')
@app.route('/index')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/search')
def search():
    form = SearchForm()
    return render_template('search.html', form=form)

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/contributors')
def contributors():
    return render_template('contributors.html')