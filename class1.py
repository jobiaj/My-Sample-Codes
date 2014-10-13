from math import *
class Coordinate(object):
        def __init__(self,x,y):
                self.x = x
                self.y = y

c = Coordinate(2,3)
orgin = Coordinate(0,0)
d = sqrt(((c.x)**2 - (orgin.x)**2) + ((c.y)**2 - (orgin.y)**2))
print d
e = Coordinate()
e.init(3,2)


