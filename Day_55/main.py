from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return "u" + func() + "</em>"
    return "u" + func() + "/u"


@app.route("/")
def hello():
    return "<h1 style='text-align: center;'>Hello world!</h1>"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
