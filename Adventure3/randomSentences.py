#coding: utf-8
import Tkinter as tk
import  random

def randomNoun():
    nonus = ["cats", "hippos", "cakes"]
    noun = random.choice(nonus)
    return noun

def randomVerb():
    verbs = ["eats", "likes", "hates", "has"]
    verb = random.choice(verbs)
    return verb

window = tk.Tk()

def createSentence():
    name = nameEntry.get()
    noun = randomNoun()
    verb = randomVerb()
    sentence = name + " " + verb + " " + noun
    result.config(text = sentence)

nameLabel = tk.Label(window, text = "Name:")
nameEntry = tk.Entry(window)
button = tk.Button(window, text = "Create", \
        command = createSentence)
result = tk.Label(window)


nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()

window.mainloop()
