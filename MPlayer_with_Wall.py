import tkinter as tk
from pygame import mixer
import os
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")

mixer.init()

songs = []
for song in os.listdir("E:\Data Structure\Python_Music\Music"):
    if song.endswith(".mp3"):
        songs.append(song)

def play_song():
    song = songs[listbox.curselection()[0]]
    mixer.music.load(song)
    mixer.music.play()

def pause_song():
    mixer.music.pause()

def stop_song():
    mixer.music.stop()

def skip_song():
    next_song = listbox.curselection()[0] + 1
    if next_song == len(songs):
        next_song = 0
    mixer.music.stop()
    play_song(songs[next_song])

listbox = tk.Listbox(root)
for song in songs:
    listbox.insert(tk.END, song)

image = ImageTk.PhotoImage(Image.open("E:/Data Structure/Python_Music/IMAGE.png"))
background_label = tk.Label(root, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

play_button = tk.Button(root, text="Play", command=play_song)
pause_button = tk.Button(root, text="Pause", command=pause_song)
stop_button = tk.Button(root, text="Stop", command=stop_song)
skip_button = tk.Button(root, text="Skip", command=skip_song)

play_button.pack()
pause_button.pack()
stop_button.pack()
skip_button.pack()

listbox.pack()

root.mainloop()
