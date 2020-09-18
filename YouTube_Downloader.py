from tkinter import *
import os
from pytube import YouTube
import youtube_dl

root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("logo.ico")

toplabel = Label(
    root, text="Enter the Youtube URL you'd like to download and choose a file format to save it")
toplabel.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=100)
e.grid(row=1, column=0, columnspan=2)


def download_mp3():
    video_url = e.get()
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=video_url, download=False
        )
        filename = os.path.join('mp3 downloads', f"{video_info['title']}.mp3")
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        mp3_label = Label(
            root, text=f"#DOWNLOAD SUCCESSFUL# {filename}", bg="#7CCD7C")
        mp3_label.grid(row=3, column=0, columnspan=2)
    except Exception as error:
        if filename:
            mp3_label = Label(
                root, text=f"#DOWNLOAD SUCCESSFUL# {video_info['title']}.mp3", bg="#7CCD7C")
            mp3_label.grid(row=3, column=0, columnspan=2)
        else:
            error_label = Label(
                root, text=f"#DOWNLOAD ERROR# {error}", bg="#e50000", fg='white')
            error_label.grid(row=3, column=0, columnspan=2, rowspan=2)


def download_mp4():
    url = e.get()
    try:
        mp4_file = YouTube(url).streams.first().download(os.path.join(
            "mp4 downloads"))
        filename = str(mp4_file).split('\\')[-1]
        mp4_label = Label(
            root, text=f"#DOWNLOAD SUCCESSFUL# {filename}", bg="#7CCD7C")
        mp4_label.grid(row=3, column=0, columnspan=2)
    except Exception as error:
        error_label = Label(
            root, text=f"#DOWNLOAD ERROR# {error}", bg="#e50000", fg='white')
        error_label.grid(row=3, column=0, columnspan=2, rowspan=2)


button1 = Button(root, text="MP3", padx=50, pady=15,
                 command=download_mp3,  bg='#0198E1', fg='white')
button2 = Button(root, text="MP4", padx=50, pady=15,
                 command=download_mp4, bg='#0D4F8B', fg='white')


button1.grid(row=2, column=0, columnspan=1)
button2.grid(row=2, column=1, columnspan=1)

root.mainloop()
