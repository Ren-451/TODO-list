# package import
from tkinter import *
import tkinter.messagebox

window = Tk()

# give title
window.title("TODO List App")

# frame widget
frame_task = Frame(window)
frame_task.pack()

# hold item in listbox
listbox_task = Listbox(frame_task, bg="#096578", fg="#91e1f0", height=15, width=50, font="Source Code Pro")
listbox_task.pack(side=tkinter.LEFT)

window.mainloop()
