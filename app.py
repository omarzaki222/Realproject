from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>fo2 tt7t ymen shmal</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)