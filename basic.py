from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello im a home page</h1>"


@app.route("/information")
def info() -> str:
    return "<h2>Return other page in flask</h2>"


@app.route("/user/<name>")
def user(name: str) -> str:
    return f"<h1>This is a page for {name.capitalize()}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
