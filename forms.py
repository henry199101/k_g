from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField


class SearchForm(FlaskForm):
    search_content = StringField('Search_content')
    search_button = SubmitField('Search it !')
    pull_down_list = SelectField(u'Program', choices=[('py', 'python'), ('text', 'plain text')])