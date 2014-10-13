
from math import *
class Coordinate(object):
        def __init__(self,x,y):
                self.x = x
                self.y = y
	def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        	return self.x

   	def getY(self):
        # Getter method for a Coordinate object's y coordinate
        	return self.y

	def __str__(self):

		return "(" + str(self.x) + "," + str(self.y) +")"
	def __eq__(self):
		if(str(self.x)==str(self.y)):
			return True
c = Coordinate(2,2)
print Coordinate.getX(c)
print Coordinate.eq(c)



