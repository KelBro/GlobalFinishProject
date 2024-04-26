from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField,  SubmitField, EmailField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    boolField = BooleanField("Вы преподаватель?")
    select = SelectField('Направления',
                         choices=[('vol', 'Волонтёрство'), ('sp', 'Спорт'), ('na', 'Наука'), ('tv', 'Творчество')])
    submit = SubmitField('Зарегистрироваться')
