#coding: utf-8
import Tkinter as tk
window = tk.Tk()

def showNumber(source): # 括号内必须要有一个参数，可以没有实际用处
    num = slider.get()
    label.config(text = str(num))

slider = tk.Scale(window, from_=0, to = 100, \
        command = showNumber)
label = tk.Label(window)


slider.pack()
label.pack()

window.mainloop()
