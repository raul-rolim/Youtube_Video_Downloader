from pytube import YouTube
from tkinter import *

root = Tk()
root.title('Youtube Video Downloader')
root.geometry('350x150')
root.resizable(width=False, height=False)

#yt = YouTube()

def download_option():
    global download_button, exit_button, url_user, return_button
    global download_video
    download_button.grid_forget()
    exit_button.grid_forget()
    url_user = Entry(button_frame, text="Insert Your Url")
    download_video = Button(button_frame, text="Download", command = lambda:download(url_user.get()))
    return_button = Button(button_frame, text="Return", command = forget)
    url_user.grid(row=0, column=0)
    download_video.grid(row=0, column=1, padx=10)
    return_button.grid(row=1, column=2, padx=10)
def download(user_url_input):
    url = str(user_url_input)
    my_video = YouTube(url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()

def menu():
    global download_button, exit_button, button_frame

    button_frame = LabelFrame(root, text="Buttons", padx=10, pady=10)
    button_frame.pack()
    download_button = Button(button_frame, text="Download a Video", command= download_option)
    exit_button = Button(button_frame, text="EXIT", command=exit)
    download_button.grid(row=0, column=0, padx=10)
    exit_button.grid(row=0, column=1, padx=10)

def forget():
    global download_button, button_frame, url_user, return_button
    global download_video
    download_button.grid_forget()
    url_user.grid_forget()
    return_button.grid_forget()
    download_video.grid_forget()
    button_frame.pack_forget()
    menu()

menu()
root.mainloop()