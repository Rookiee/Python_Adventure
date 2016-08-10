#coding: utf-8

import Tkinter as tk

window = tk.Tk()

def checkPassword():
    password = "ByeBye"
    enteredPassword = passEntry.get()
    if enteredPassword == password:
        confirmLabel.config(text = "Correct")
    else:
        confirmLabel.config(text = "Incorrect")

# cerate button
button = tk.Button(window, text = "Login", \
        command = checkPassword)
# just a label showing "password: "
passwordLabel = tk.Label(window, text = "Password: ")
# create a entry, all the characters typed will be displayed as *
passEntry = tk.Entry(window, show = "*")  # 注意show
# just a label used to indicate correct or incorrect
confirmLabel = tk.Label(window)

# the order of the following are significant
passwordLabel.pack()
passEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()
