# coding:utf-8

from flask import Flask, redirect, url_for, render_template, flash
from forms import SearchForm, DeleteKnowledgeForm, NewKnowledgeForm
from flask_sqlalchemy import SQLAlchemy
import os, click

app = Flask(__name__)
app.secret_key = 'secret string'

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def index():
    return redirect(url_for('search'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)

@app.route('/result', methods=['GET', 'POST'])
def result():
    form = SearchForm()
    knowledges = KnowledgeTable.query.filter_by(entity='Li He')
    return render_template('result.html', knowledges=knowledges, form=form)


@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/contributors')
def contributors():
    return render_template('contributors.html')

@app.route('/new', methods=['GET', 'POST'])
def new_knowledge():
    form = NewKnowledgeForm()
    if form.validate_on_submit():
        entity      = form.entity.data
        attr_name   = form.attr_name.data
        attr_value  = form.attr_value.data
        knowledge   = KnowledgeTable(entity=entity, attr_name=attr_name, attr_value=attr_value)
        db.session.add(knowledge)
        db.session.commit()
        flash('A knowledge has been uploaded!')
        return redirect(url_for('index'))
    return render_template('admin.html', form=form)

@app.cli.command()
def initdb():
    db.create_all()
    click.echo('数据库初始化完毕！')

class KnowledgeTable(db.Model):
    entity      = db.Column(db.Text, name='entity', primary_key=True)
    attr_name   = db.Column(db.Text, name='attr_name')
    attr_value  = db.Column(db.Text, name='attr_value')

    def __repr__(self):
        return self.__class__.__name__ + '\'s entity: %r' % self.entity