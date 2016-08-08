import turtle
import random

import turtle

def DrawShape(sides, length):
	angle = 360.0 / sides
	for sides in range(sides):
		turtle.forward(length)
		turtle.left(angle)

def MoveTurtle(x, y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()

def DrawSquare(length):
	DrawShape(4, length)

def DrawTriangle(length):
	DrawShape(3, length)

def DrawCircle(length):
	DrawShape(360, length)


def DrawRandomShapes():
	x = random.randrange(-200, 200)
	y = random.randrange(-200, 200)
	length = random.randrange(70)
	shape = random.randrange(1,4)

	MoveTurtle(x,y)
	if shape == 1:
		DrawSquare(length)
	elif shape == 2:
		DrawTriangle(length)
	else :
#		length = length % 4
#		DrawCircle(length)
		turtle.circle(length)

if __name__ == '__main__':
	for shape in range(100):
		DrawRandomShapes()
	turtle.done()
