from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchForm(FlaskForm):
    search_content = StringField('Search_content')
    search_button = SubmitField('Search it !')