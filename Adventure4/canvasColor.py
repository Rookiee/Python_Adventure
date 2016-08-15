#coding: utf-8
import Tkinter as tk

window = tk.Tk()


def sliderUpdate(source):
    red = redSlider.get()
    green = greenSlider.get()
    blue = blueSlider.get()

    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg = color)
    displayColorEntry.delete(0, tk.END)
    displayColorEntry.insert(0, str(color))

redSlider = tk.Scale(window, from_ = 0, to = 255,\
        command = sliderUpdate)
greenSlider = tk.Scale(window, from_ = 0, to = 255,\
        command = sliderUpdate)
blueSlider = tk.Scale(window, from_ = 0, to = 255, \
        command = sliderUpdate)

canvas = tk.Canvas(window, width = 300, height = 300)

redLabel = tk.Label(window, text = "Red")
greenLabel = tk.Label(window, text = "Green")
blueLabel = tk.Label(window, text = "Blue")

displayColorEntry = tk.Entry(window)

redLabel.grid(row = 1, column = 1)
greenLabel.grid(row = 1, column = 2)
blueLabel.grid(row = 1, column = 3)

redSlider.grid(row = 2, column = 1)
greenSlider.grid(row =2 , column = 2)
blueSlider.grid(row = 2, column = 3)
canvas.grid(row = 3, column = 1, columnspan = 3)
displayColorEntry.grid(row = 4, column = 1, columnspan = 3)
# displayColorEntry.grid(row = 4, column = 1)

tk.mainloop()

canvas.pack()
tk.mainloop()
