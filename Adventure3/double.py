#coding: utf-8
import Tkinter as tk


def changeString():
    stringToCopy = entry.get()
    entry.insert(0, stringToCopy)

def insertChar():
    character = "b"
    entry.insert(3, character)

window = tk.Tk()

entry = tk.Entry(window)
button = tk.Button(window, text = "Clikc", \
        command = changeString)

insertButton = tk.Button(window, text = "Insert",\
        command = insertChar)

entry.pack()
button.pack()
insertButton.pack()
window.mainloop()




