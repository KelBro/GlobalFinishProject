from flask import Flask, render_template, url_for, redirect
from data import db_session
from data.students import Student
from forms.register_student import RegisterForm

# Создаем экземпляр приложения Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretni_kodik'


# Главная страница
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# Страница входа
@app.route("/login")
def login():
    return render_template("logining.html")


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
    db_session.global_init("db/blogs.db")
    # Запуск сервера Flask
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
