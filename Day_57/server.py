from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

agify_url = "https://api.agify.io?name="
gender_url = "https://api.genderize.io?name="


def get_gender(name: str):
    response = requests.get(gender_url + name).json()
    return response


def get_age(name: str):
    response = requests.get(agify_url + name).json()
    return response


@app.route("/")
def home_page():
    year = datetime.datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", rand_num=random_number, year=year)


@app.route("/guess/<string:name>")
def guess_gender_and_age(name):
    gender = get_gender(name)["gender"]
    age = get_age(name)["age"]
    return render_template("guess.html", gender=gender, age=age, name=name)


@app.route("/blog/<num>")
def get_blog(num):
    posts_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(posts_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
