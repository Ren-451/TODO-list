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

# scrolldown
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# button
enter_button = Button(window, text="Add", width=50, command=entertask)
enter_button.pack(pady=3)

del_button = Button(window, text="Delete", width=50, command=deletetask)
del_button.pack(pady=3)

done_button = Button(window, text="Done", width=50, command=donetask)
done_button.pack(pady=3)

window.mainloop()
