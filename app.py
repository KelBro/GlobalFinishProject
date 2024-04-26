from flask import Flask, render_template, url_for, redirect, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.__all_models import students, clubs, request
from forms.add_club import ClubForm
from forms.register_student import RegisterForm, LoginForm
from forms.add_request import RequestSubmit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretni_kodik'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.get(students.Student, user_id)


# Главная страница
@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    clubss = db_sess.query(clubs.Clubs).all()
    db_sess.close()
    return render_template("index.html", clubs=clubss)


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
        user = db_sess.query(students.Student).filter(students.Student.email == form.email.data).first()
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
        if db_sess.query(students.Student).filter(students.Student.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        # Создаем нового пользователя
        user = students.Student(
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


# Создание нового кружка
@app.route('/club/create', methods=['GET', 'POST'])
@login_required
def add_club():
    form = ClubForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(clubs.Clubs).filter(clubs.Clubs.title == form.title.data).first():
            return render_template('add_club.html', title='Добавление кружка',
                                   form=form,
                                   message="Такой кружок уже есть")
        teacher_name = current_user.name
        type_club = current_user.name_club

        club = clubs.Clubs(
            title=form.title.data,
            teacher_name=teacher_name,
            about=form.about.data,
            type=type_club
        )

        db_sess.add(club)
        db_sess.commit()
        return redirect('/')
    return render_template('add_club.html', title='Добавление кружка', form=form)


@app.route('/request/<club>', methods=['GET', 'POST'])
@login_required
def requesttt(club):
    form = RequestSubmit()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(request.Request).filter(request.Request.name_club == club and request.Request.student == current_user.name).first():
            return render_template('send_request.html', form=form,
                                   message="Нельзя отправить заявку более одного раза")
        else:
            requestt = request.Request(
                student=current_user.name,
                name_club=club,
                information=form.text.data
            )
            db_sess.add(requestt)
            db_sess.commit()
            return redirect(f"/")
    return render_template('send_request.html', form=form)


@app.route('/requests')
@login_required
def requests():
    db_sess = db_session.create_session()
    requestss = db_sess.query(request.Request).filter(request.Request.student == current_user.name)
    db_sess.close()
    return render_template("requests.html", requests=requestss)


def main():
    # Инициализация базы данных
    db_session.global_init("db/vvgu_clubs_bd.db")
    # Запуск сервера Flask
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
