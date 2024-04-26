from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, IntegerField, BooleanField, \
    SelectField
from wtforms.validators import DataRequired


class RequestSubmit(FlaskForm):
    text = StringField('Почему именно ты?', validators=[DataRequired()])
    submit = SubmitField('Подать заявку')

