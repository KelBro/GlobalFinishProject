from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(index(debug=True))
