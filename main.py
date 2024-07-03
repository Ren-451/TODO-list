# package import
from tkinter import *
import tkinter.messagebox

window = Tk()

# give title
window.title("TODO List App")

# interface

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
entry_button = Button(window, text="Add", width=50, command=entertask)
entry_button.pack(pady=3)

del_button = Button(window, text="Delete", width=50, command=deletetask)
del_button.pack(pady=3)

done_button = Button(window, text="Done", width=50, command=donetask)
done_button.pack(pady=3)

# definitions


def entertask():

    # new popup window to create task
    input_text = ""

    def add():

        input_text = entry_task.get(1.0, "end - 1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning.", message="Please enter text.")
        else:
            listbox_task.insert(END, input_text)
            # close root1 window
            root1.destroy()

    root1 = Tk()
    root1.title("Add a task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add a task", command=add)
    button_temp.pack()
    root1.mainloop()

def deletetask():

    # delete selected
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

    # is executed to mark done

window.mainloop()
