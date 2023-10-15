from pytube import YouTube
from tkinter import *

root = Tk()
root.title('Youtube Video Downloader')
root.geometry('650x400')
root.resizable(width=False, height=False)

#yt = YouTube()

def download_option():
    global download_button, exit_button
    download_button.grid_forget()
    exit_button.grid_forget()
    url_user = Entry(button_frame, text="Insert Your Url")
    download_video = Button(button_frame, text="Download", command = lambda:download(url_user.get()))
    url_user.grid(row=0, column=0)
    download_video.grid(row=0, column=1, padx=10)
def download(user_url_input):
    url = str(user_url_input)
    my_video = YouTube(url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()
def menu():
    global download_button, exit_button, button_frame

    text_frame = LabelFrame(root, text="Frame", padx=10, pady=10)
    button_frame = LabelFrame(root, text="Buttons", padx=10, pady=10)
    text_frame.pack()
    button_frame.pack()
    download_button = Button(button_frame, text="Download a Video", command= download_option)
    exit_button = Button(button_frame, text="EXIT", command=exit)
    download_button.grid(row=0, column=0, padx=10)
    exit_button.grid(row=0, column=1, padx=10)

menu()
root.mainloop()