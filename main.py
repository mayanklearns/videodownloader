import pytube
from pytube.cli import on_progress
from flask import Flask, render_template, request, send_file, redirect

app = Flask(__name__)
def downloadvideo(url):
    youtube = pytube.YouTube(url, on_progress_callback=on_progress)
    video = youtube.streams.filter(progressive=True, res = "720p").first()
    filename = video.title
    filesizeinmb = video.filesize/1000000
    fileurl = video.url
    return fileurl

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        url = request.form["link"]
        youtube = pytube.YouTube(url, on_progress_callback=on_progress)
        video = youtube.streams.filter(progressive=True, res = "720p").first()
        filename = video.title
        filesizeinmb = video.filesize/1000000
        fileurl = video.url
        return redirect(fileurl)

if __name__ == "__main__":
    app.run(debug=True)
