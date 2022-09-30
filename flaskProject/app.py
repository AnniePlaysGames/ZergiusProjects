from flask import Flask

from views import MainView

app = Flask(__name__)
app.config.from_pyfile("config.py")

MainView.register(app)


if __name__ == '__main__':
    app.run()
