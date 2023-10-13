from pytube import YouTube
from tkinter import *

root = Tk()
root.title('Youtube Video Downloader')
root.geometry('650x400')

yt = YouTube()

def downloader(user_url_input):
    url = str(user_url_input)
    my_video = YouTube(url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download()

def menu():
    print("Welcome To The Youtube Video Downloader")
    running = True
    while running:
        choice = int(input("MENU\n1 - Download a Video\n2 - Exit"))

        if choice == 1:
            user_url = input("Insert the Video's Url: ")
            downloader(user_url)
        elif choice == 2:
            exit()
        else:
            print("Invalid Choice! Try Again\n")


root.mainloop()