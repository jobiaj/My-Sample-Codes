from math import *
class Coordinate(object):
        def __init__(self,x,y):
                self.x = x
                self.y = y
        def __str__(self):
                return "(" + str(self.x) + "," + str(self.y) +")"

c = Coordinate(2,4)
d = Coordinate(0,0)
e = (1,22)
print c
print d
print type(c)
print isinstance(c,Coordinate)
print isinstance(e, Coordinate)                                  
