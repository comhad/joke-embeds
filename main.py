from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def home() :
    return open("templates/homepage.html","r").read() # Not bothering with rendering, no variables

@app.route("/yt")
def youtube() :
    renderDict = {}
    videoId = request.args.get("video", default="")
    renderDict["id"] = videoId
    soup = BeautifulSoup(requests.get("https://youtube.com/watch?v=" + videoId).text, 'html.parser')
    splitTitle = soup.title.string.split("-")
    splitTitle.pop()
    renderDict["title"] = "-".join(splitTitle)
    return render_template("embeds/youtube.html", renderDict=renderDict)