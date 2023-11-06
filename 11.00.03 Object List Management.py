from math import pi

class Ball():

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
class BallList ():
	
# Step 2 - Define the initializer and any default values
	def __init__(self):

# Step 3 - Define the object attributes
# Create an empty ball list
		self.Balllist = []

# Step 4 - Define Actions (Methods) associated with the object
# Add a ball to the list
	def add_ball(self, balltype="Basketball", diameter=9.51, pressure=8.0):
#		Create a new ball object
		myball = Ball(balltype, diameter, pressure)
#		Append ball object to list
		self.Balllist.append(myball)

	def delete_ball(self, balltype):
		index = self.find_ball(balltype)
		del self.Balllist[index]
		
	def change_pressure(self, balltype, pressurechange):
		index = self.find_ball(balltype)
		self.Balllist[index].Pressure += pressurechange
		return self.Balllist[index].Pressure

	def find_ball(self, balltofind):
		for i in range(len(self.Balllist)):
			if self.Balllist[i].BallType == balltofind:
				return i
		return -1		

	def number_of_balls(self):
		return len(self.Balllist)

	def print_ball_list(self):
		print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Type", "Diameter", "Pressure", "Circumference"))
		for i in range(len(self.Balllist)):
			print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(self.Balllist[i].BallType, self.Balllist[i].Diameter, self.Balllist[i].Pressure, self.Balllist[i].Circumference()))
		print()
		print("{} balls in list".format(self.number_of_balls()))
		print()

	def add_ball_from_file(self, filename):
		ballfile = open(filename)
		x = ballfile.readline()
		while x != "":
			y = x.split(",")
			self.add_ball(y[0].strip(), float(y[1].strip()), float(y[2].strip()))
			x = ballfile.readline()
		ballfile.close()

myballlist = BallList()
myballlist.add_ball_from_file("11.00.01 Balls.txt")
myballlist.print_ball_list()
myballlist.change_pressure("Basketball", 1)
myballlist.change_pressure("Volleyball", -1)
myballlist.add_ball("Baseball", 2.75, 0.0)
print()
myballlist.print_ball_list()
myballlist.delete_ball("Soccerball")
myballlist.print_ball_list()