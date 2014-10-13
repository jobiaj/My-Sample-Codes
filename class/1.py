from math import *

class Coordinate(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "("+str(self.x)+ ","+str(self.y)+")"
	def distance(self,other):
		return sqrt((self.x-other.x)**2 + (self.y - other.y)**2) 
c = Coordinate(3,4)
d = Coordinate(0,0)
print Coordinate.distance(c,d)
