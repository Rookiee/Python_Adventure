#coding: utf-8
import Tkinter as tk
import random

window  = tk.Tk()

score = 0
maxNo = 10
rounds = 0

def buttonClick():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        if 0 < guess <= maxNo:
            result = random.randrange(1, maxNo+1)
            if guess == result:
                score = score +1
            rounds = rounds +1
        else:
            result = "Entry not valid"
    except:
        result = "Entry not valid"
    resultLabel.config(text = result)
    scoreLabel.config(text = str(score) + "/" + str(rounds))
    guessBox.delete(0, tk.END)

showLabel = tk.Label(window, text = "Enter a number from 0 to 10:")
guessBox = tk.Entry(window)
resultLabel = tk.Label(window)
scoreLabel = tk.Label(window)
button = tk.Button(window, text = "GUESS", \
        command = buttonClick)

showLabel.pack()
guessBox.pack()
resultLabel.pack()
scoreLabel.pack()
button.pack()

window.mainloop()
