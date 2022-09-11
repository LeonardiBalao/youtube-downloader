from pytube import YouTube
import os

def downloadYouTube(videoURL, path):

    yT = YouTube(videoURL)
    yT = yT.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yT.download(path)

downloadYouTube('https://www.youtube.com/watch?v=tsNswx0nRKM&list=PLj-4DlPRT48k8TZ2ZjzbjnAq_wgIwsIab&index=3&ab_channel=LamaDev', './')