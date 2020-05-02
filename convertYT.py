__author__ = "Trang Ha"

# Link to Download ffmpeg packet: https://www.ffmpeg.org/download.html
import youtube_dl

def convertToMP3(link):
    downloadSetting = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320"
        }]
    }
    with youtube_dl.YoutubeDL(downloadSetting) as ydl:
        ydl.download([link])

while True:
    inputLink = input("Enter URL: " + " ")
    if inputLink == "":
        print("Please enter appropriate link!")
    else:
        convertToMP3(inputLink)