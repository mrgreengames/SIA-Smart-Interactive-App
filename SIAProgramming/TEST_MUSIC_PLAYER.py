import os
import pygame
from mutagen.id3 import ID3
from tkinter import *
from tkinter.filedialog import askdirectory


root = Tk()
root.minsize(300,300)

listofsongs = []
realnames =[]

index = 0

def nextsong(event):
    global index

    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def prevsong(event):
    global index
    index-=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def stopsong(event):
    pygame.mixer.music.stop()


def directorychooser():

    directory=askdirectory()
    if directory=='':
        print('No files were entered')
        pass
    else:
        os.chdir(directory)
        for files in os.listdir(directory):
            if files.endswith(".mp3"):

                realdir = os.path.realpath(files)
                realnames.append(files)
                listofsongs.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

label=Label(root,text="Music Player")
label.pack()
listbox =Listbox(root)
listbox.pack()

realnames.reverse()

for i in realnames:
    listbox.insert(0,i)

listofsongs.reverse()

nextbutton=Button(root,text= "Next Song")
nextbutton.pack()
previousbutton=Button(root,text="Previous Song")
previousbutton.pack()
stopbutton=Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)



if __name__=="__main__":
    root.mainloop()
