from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "hello world"


if __name__ == "__main__"git push - u origin master:
    app.run(debug=True, threaded=True)
