from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    name = "Manuel"
    letters = list(name)
    my_list = [1, 2, 3, 4, 5]
    return render_template("basic.html", my_variable=name, letters=letters, my_list=my_list)


if __name__ == "__main__":
    app.run(debug=True)
