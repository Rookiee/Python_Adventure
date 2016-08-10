#coding: utf-8
import Tkinter as tk

count  = 0
def buttonClicked():
    global count
    count = count + 1
    button.config(text = str(count) )

window = tk.Tk()
button = tk.Button(window, text = "Click me", \
        command = buttonClicked)
button.pack()
window.mainloop()
