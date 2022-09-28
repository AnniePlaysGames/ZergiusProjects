from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for("index"))
    return render_template("index.html")


@app.route('/about/<int:username>')
def about(username: str):
    return render_template("about.html", username = username)


if __name__ == '__main__':
    app.run(debug=True)
