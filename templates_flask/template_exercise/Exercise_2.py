# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# This page will be the page after the form
@app.route("/report")
def report():
    # Check the user name for the 3 requirements.
    letters = request.args.get("UserName")
    requirement = dict()
    for letter in letters:
        if letter.isupper():
            requirement["is_upper"] = 1
        elif letter.islower():
            requirement["is_lower"] = 1

    requirement["is_num"] = 1 if letters[-1].isdigit() else 0

    return render_template(
        "report.html",
        requirements=sum(requirement.values()),
        lower=requirement.get("is_lower"),
        upper=requirement.get("is_upper"),
        num_end=requirement.get("is_num"),
    )


if __name__ == "__main__":
    # Fill this in!
    app.run(debug=True)
