import turtle 
import math

print('Starting TurtleDraw_di.py by Darko Ilic')

input ('Hello. Type in the name of the data file you wish to use.   ')
DATAFILE = 'turtle-draw.txt'



turtleDarko = turtle.Screen()
turtleDarko.setup(450, 450)

turtleDrake = turtle.Turtle()
turtleDrake.speed(10)
turtleDrake.penup()

total_distance = 0
lastPosition = None

turtleDrakeDatafile = open(DATAFILE, 'r')
line = turtleDrakeDatafile.readline()
while line:
	print(line, end='')
	parts = line.split(' ')

	if (len(parts) == 3):
		color = parts[0]
		x = int(parts[1])
		y = int(parts[2])
		lastPosition = None

		if lastPosition is not None:
			total_distance += math.hypot(x - lastPosition[0], y - lastPosition[1])

		turtleDrake.color(color)
		turtleDrake.goto(x,y)
		turtleDrake.pendown()

	if (len(parts) == 1): 
		turtleDrake.penup()

	line = turtleDrakeDatafile.readline()

turtleDrake.penup()
turtleDrake.goto(200, -200)
turtleDrake.write(f'Total distance: {total_distance:.2f}', align='right')


turtle.done()
turtleDrakeDatafile.close()

print('\nEnd - Press the Enter key to exit the program')
input()