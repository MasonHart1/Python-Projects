import os
from tkinter import *
import pygame

root = Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init()

songlist = Listbox(root, bg="black", fg="white", width=100, height=15, font="Arial 12")
songlist.pack(padx=25, pady=10)

root.mainloop()