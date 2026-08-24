import os
from tkinter import filedialog as fd
from tkinter import *
import pygame
import subprocess

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

    songs.clear()
    songlist.delete(0, END)

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            full_path = os.path.join(root.directory, song)
            songs.append(full_path)
            songlist.insert("end", name)

    if songs:
        songlist.selection_set(0)
        current_song = songs[0]


def on_song_select(event):
    global current_song
    selected_index = songlist.curselection()
    if selected_index:
        index = selected_index[0]
        current_song = songs[index]


def load_song():
    global current_song
    root.file = fd.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

    if root.file:
        name = os.path.basename(root.file)
        display_name = os.path.splitext(name)[0]

        songs.append(root.file)
        songlist.insert("end", display_name)

organize_menu = Menu(menubar, tearoff=False)
organize_menu.add_command(label="Select Folder", command=load_music)
organize_menu.add_command(label="Select Song", command=load_song)
menubar.add_cascade(label="Add Music", menu=organize_menu)

songlist = Listbox(root, bg="black", fg="white", width=100, height=15, font="Arial 12")
songlist.pack(padx=25, pady=10)

songlist.bind("<<ListboxSelect>>", on_song_select)

buttons = [
    ("Previous", lambda: play_previous_song(), "Musicplayer/pictures/previous.png"),
    ("Play", lambda: play_music(), "Musicplayer/pictures/play.png"),
    ("Pause", lambda: pause_music(), "Musicplayer/pictures/pause.png"),
    ("Next", lambda: play_next_song(), "Musicplayer/pictures/next.png")
]

control_frame = Frame(root)
control_frame.pack()

# Control buttons
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
    paused = False

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
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
    paused = False
    

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def onclosing():
    pygame.mixer.music.stop()
    root.destroy()
    subprocess.run(['python', 'main.py'])

root.protocol("WM_DELETE_WINDOW", onclosing)

root.mainloop()