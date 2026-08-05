import os
from tkinter import filedialog as fd
from tkinter import *
import pygame

root = Tk()
root.title("Music Player")
root.geometry("437x366")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
current_song= ''
paused = False

def load_music():
    global current_song
    root.directory = fd.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(name)

    for song in songs:
        songlist.insert("end", song)
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

organize_menu = Menu(menubar, tearoff=False)
organize_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Organize", menu=organize_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15, font="Arial 12")
songlist.pack(padx=25, pady=10)

buttons = [
    ("Previous", lambda: play_previous_song(), "Musicplayer/pictures/previous.png"),
    ("Play", lambda: play_music(), "Musicplayer/pictures/play.png"),
    ("Pause", lambda: pause_music(), "Musicplayer/pictures/pause.png"),
    ("Next", lambda: play_next_song(), "Musicplayer/pictures/next.png")
]

control_frame = Frame(root)
control_frame.pack()

for i, (name, command, image_path) in enumerate(buttons):
    img = PhotoImage(file=image_path)

    btn = Button(
        control_frame,
        image=img,
        command=command,
        borderwidth=0
    )
    btn.image = img  # Prevent garbage collection
    btn.grid(row=5, column=i, padx=7, pady=10)


def play_next_song():
    global current_song, paused

    if not songs.index(current_song) == len(songs) - 1:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    else:
        songlist.selection_clear(0, END)
        songlist.selection_set(0)
        current_song = songs[0]
        play_music()

def play_previous_song():
    global current_song, paused

    if not songs.index(current_song) == 0:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    else:
        songlist.selection_clear(0, END)
        songlist.selection_set(len(songs) - 1)
        current_song = songs[-1]
        play_music()

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song+'.mp3'))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
    paused = False
    

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

root.mainloop()