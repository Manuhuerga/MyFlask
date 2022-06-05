# Note we imported request!
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# This page will have the sign up form
@app.route("/signup")
def signup():
    return render_template("signup.html")


# This page will be the page after the form
@app.route("/thankyou")
def thankyou():
    first = request.args.get("first")
    last = request.args.get("last")
    return render_template("thankyou.html", first=first, last=last)


@app.errorhandler(404)
def error(e):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
