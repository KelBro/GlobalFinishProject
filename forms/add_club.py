from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    teacher_name = TextAreaField("ФИО сотрудника")
    about = TextAreaField("Содержание")
    type = TextAreaField("Направление")
    submit = SubmitField('Применить')
