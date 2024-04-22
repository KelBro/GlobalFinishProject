from flask import Flask, render_template, url_for, redirect
from flask_login import LoginManager, login_user, login_required, logout_user

from data import db_session
from data.clubs import Clubs
from data.students import Student
from forms.register_student import RegisterForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretni_kodik'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(Student).get(user_id)


# Главная страница
@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    clubs = db_sess.query(Clubs).all()
    db_sess.close()
    return render_template("index.html", clubs=clubs)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Student).filter(Student.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('signing.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('signing.html', form=form)


# О странице
@app.route("/about")
def about():
    return render_template("about.html")


# Регистрация нового пользователя
@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        # Создаем новую сессию базы данных
        db_sess = db_session.create_session()
        # Проверяем, существует ли пользователь с таким email
        if db_sess.query(Student).filter(Student.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        # Создаем нового пользователя
        user = Student(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            is_teacher=form.boolField.data,
            name_club=form.select.data,
        )
        user.set_password(form.password.data)
        # Добавляем пользователя в базу данных и сохраняем изменения
        db_sess.add(user)
        db_sess.commit()
        # Перенаправляем на страницу входа
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    # Инициализация базы данных
    db_session.global_init("db/vvgu_clubs_bd.db")
    # Запуск сервера Flask
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
