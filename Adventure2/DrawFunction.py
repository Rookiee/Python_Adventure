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
	DrawShape(length)

def DrawCircle(length):
	DrawShape(360, length)

if __name__ ==  '__main__':
	DrawShape(4, 20)
	MoveTurtle(-20,0)
	DrawShape(360,1)
	turtle.done()
