import turtle
import time
length = 1
angle = 1
count = 0

turtle.fillcolor("yellow")
turtle.begin_fill()
while count < 360:
	turtle.forward(length)
	turtle.left(angle)
	count += 1
turtle.end_fill()

turtle.done()
