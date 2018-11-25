from tkinter import *
from tkinter import ttk

root = Tk()

root.title('Hello, Tkinter!')
root.geometry('300x400')

frame = Frame(root)

labelText = StringVar()
labelText.set("I am a Label")
label = Label(frame, textvariable=labelText)


button = Button(frame, text="Click Me")


label.pack()
button.pack()
frame.pack()

root.mainloop()