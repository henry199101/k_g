# coding:utf-8


from flask import Flask, render_template
from forms import SearchForm
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.secret_key = 'secret string'

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



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

class KnowledgeTable(db.Model):
    entity      = db.Column(db.Text, name='entity', primary_key=True)
    attr_name   = db.Column(db.Text, name='attr_name')
    attr_value  = db.Column(db.Text, name='attr_value')