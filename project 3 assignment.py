import turtle
from itertools import cycle
colors=cycle(['red','orange','yellow','blue','purple'])
def draw_shape(size,angle,shift,shape):
	turtle.pencolor(next(colors))
	next_shape=''
	if shape=='square':
		turtle.circle(size)
		next_shape='square,circle'
	elif shape=='square':
		
			turtle.forward(size+2)
			turtle.left(90)
		
	turtle.right(angle)
	turtle.forward(shift)
	draw_shape(size+4,angle+1,shift+1,next_shape)
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_shape(30,0,1,'circle,square')cle')pe(30,0,1,'circle')