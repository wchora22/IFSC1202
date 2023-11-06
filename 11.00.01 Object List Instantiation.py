from math import pi
class Ball ():
	def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
		self.BallType = balltype
		self.Diameter = diameter
		self.Pressure = pressure
	def Circumference(self):
		circumference =  pi * self.Diameter
		return circumference
	def ChangePressure(self, pressurechange):
		self.Pressure += pressurechange
		return self.Pressure
def print_balllist(balllist):
	print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "Diameter", "Pressure", "Circumference"))
	for i in range(len(balllist)):
		print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(balllist[i].BallType, balllist[i].Diameter, balllist[i].Pressure, balllist[i].Circumference()))

# Finds the ball in balllist and returns the index of the row where the ball was found
def find_ball(balllist, balltofind):
	for i in range(len(balllist)):
		if balllist[i].BallType == balltofind:
			return i
	return -1		

balllist = []
ballfile = open("11.00.01 Balls.txt")
x = ballfile.readline()
while x != "":
	print(x) 
	y = x.split(",")
	print(y)
	myball = Ball(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
	balllist.append(myball)
	x = ballfile.readline()

ballfile.close()

print_balllist(balllist)
balllist[find_ball(balllist,"Basketball")].ChangePressure(1)

balllist[find_ball(balllist,"Volleyball")].ChangePressure(-1)

balllist[find_ball(balllist,"Soccerball")].Diameter = 8.01

print_balllist(balllist)