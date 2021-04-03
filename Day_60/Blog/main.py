from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/5abcca6f4e39b4955965").json()
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="bootcamp1223@gmail.com", password="Qwerty_123")
            connection.sendmail(
                from_addr="bootcamp1223@gmail.com",
                to_addrs="bootcamp1223@yahoo.com",
                msg=f"Subject:New message\n\nName: {data['name']}\nEmail: {data['email']}\n"
                    f"Phone: {data['phone']}\nMessage: {data['message']}"
            )

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
