from flask import Flask, render_template, url_for
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretni_kodik'


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("logining.html")


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
