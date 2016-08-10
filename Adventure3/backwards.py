#coding: utf-8
import Tkinter as tk

def changeOrder():
    stringToCopy = entry.get()
    stringToCopy = stringToCopy[::-1]
    entry.delete(0, tk.END)   # tk.END 表示字符串结尾
    entry.insert(0, stringToCopy)

window = tk.Tk()
entry = tk.Entry(window)
button = tk.Button(window, text = "Reverse", \
        command = changeOrder)

entry.pack()
button.pack()

window.mainloop()
