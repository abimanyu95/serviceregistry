from flask import Flask
app = Flask(__name__)


@app.route("/timer/<>")
def hello(name):
    return "Hello World!" + name

if __name__ == '__main__':
    app.run()