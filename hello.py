from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def base():
    return send_from_directory('myapp/src/', 'app.html')


@app.route("/hello")
def hello_world():
    return str("HELLLLLLLLLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")


if __name__ == "__main__":
    app.run(debug=True)
