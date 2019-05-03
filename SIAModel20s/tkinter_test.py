# tkinter test
from tkinter import *

root = Tk()
root.title("Password Test")
root.geometry("640x640+0+0")
# Password Test
name = StringVar()

label = Label(root, text="Password:", font=("georgia", 20, "bold"))
entry1 = Entry(root, textvariable=name, show="*")

label.grid(row=0, sticky=E)
entry1.grid(row=0, column=1)


def do_it():
    if str(name.get()) == "Bob":
        print("Hello Bob")
        name.__del__()
    else:
        print("You're not Bob!")
        name.__del__()


submit = Button(root, text='Submit', width=30, height=5, command=do_it).place(x=250, y=300)

root.mainloop()
