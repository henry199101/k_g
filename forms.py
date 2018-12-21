from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class SearchForm(FlaskForm):
    search_content  = StringField(label='below is a search kuang.')
    search_button   = SubmitField('Search it !')
    #pull_down_list = SelectField(u'Program', choices=[('py', 'python'), ('text', 'plain text')])


class DeleteKnowledgeForm(FlaskForm):
    submit = SubmitField('Delete')


class NewKnowledgeForm(FlaskForm):
    entity      = StringField('a entity')
    attr_name   = StringField('an attr_name')
    attr_value  = StringField('an attr_value')
    submit      = SubmitField('Upload Knowledge!')