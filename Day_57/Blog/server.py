from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


def get_posts():
    posts_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(posts_url)
    return response.json()

posts = get_posts()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route("/")
def index():
    all_posts = get_posts()
    return render_template("index.html", posts=all_posts)


@app.route("/<id>")
def get_post(id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
