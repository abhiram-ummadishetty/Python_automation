from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def youtube_downloader(yt_url,path):
    try:
        yt = YouTube(yt_url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=path)
        print("Video Downloaded!")

    except Exception as e:
        print("Invalid url")

def path_finder():
    folder = filedialog.askdirectory()
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    url = input("Enter the url of the video to be downloaded: ")
    path = path_finder()
    if path:
        print("Started download")
        youtube_downloader(url,path)
    else:
        print("Invalid link")

