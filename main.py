from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() :
    return open("static/home.html","r").read() # Not bothering with rendering, no variables