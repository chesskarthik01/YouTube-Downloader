from tkinter import *
import os
from pytube import YouTube
from pydub import AudioSegment
import ctypes
import _winapi
ctypes.windll.kernel32.SetStdHandle(_winapi.STD_INPUT_HANDLE, 0)

root = Tk()
root.title("Youtube Downloader")
root.iconbitmap("logo.ico")

toplabel = Label(
    root, text="Enter the Youtube URL you'd like to download and choose a file format to save it")
toplabel.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=100)
e.grid(row=1, column=0, columnspan=2)


def download_mp3():
    url = e.get()
    try:
        mp4_file = YouTube(url).streams.first().download(
            os.path.join('mp3 downloads'))
        destination = mp4_file.replace('mp4', 'mp3')
        mp3_file = AudioSegment.from_file(str(mp4_file))
        mp3_file.export(destination, format="mp3")
        os.remove(mp4_file)
        filename = str(destination).split('\\')[-1]
        mp3_label = Label(
            root, text=f"#DOWNLOAD SUCCESSFUL# {filename}", bg="#7CCD7C")
        mp3_label.grid(row=3, column=0, columnspan=2)
    except Exception as error:
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
