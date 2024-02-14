from flask import Flask, render_template, request
import requests
import smtplib
import socket

socket.getaddrinfo('localhost', 8080)

MY_EMAIL = "None"
MY_PASSWORD = "None"
posts = requests.get("https://api.npoint.io/bcc0899e426f137f4876").json()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", allposts=posts)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
    
