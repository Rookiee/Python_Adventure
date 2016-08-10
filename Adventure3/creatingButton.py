#coding: utf-8

import Tkinter as tk
window = tk.Tk()


def buttonClick():
    print "Beep"

def buttonClicked():
    buttonClicked.config(text = "Clicked")  # 这里的buttonClicked要和
                                            # 创建的button名字一致


button = tk.Button(window, text = "Click me", command = buttonClick)
buttonClicked = tk.Button(window, text = "Click 2", \
        command = buttonClicked)
button.pack()
buttonClicked.pack()
window.mainloop() #没有这句，运行后，窗口闪一下就消失

