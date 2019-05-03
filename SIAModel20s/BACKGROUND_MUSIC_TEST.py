# BACKGROUND MUSIC TEST
import pygame
from flask import Flask
from time import sleep
app = Flask(__name__)
from tkinter import *

@app.route("/")
def play():
    pygame.mixer.pre_init(22050, -16, 2, 4096)
    pygame.init()

    root = Tk()
    root.minsize(0,0)
    label=Label(root,text="BackGround MusicTest")

    pygame.mixer.music.load("SIA_MUSIC.wav")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
