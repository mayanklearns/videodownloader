import pytube
from pytube.cli import on_progress
from flask import Flask, render_template, request, send_file, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods = ["GET","POST"])
def download():
    if request.method == "GET":
        return render_template('download.html')
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
