class IntSet(object):
	def __init__(self):
		self.vals = []
	def insert(self,e):
		if e not in self.vals:
			 self.vals.append(e)
	def member(self, e):
		return e in self.vals
	def remove(self, e):
		if e in self.vals:
			return self.vals.remove(e)
		else:
			return "ValueError("+str(e)+"notfound"
	def __str__(self):
		self.vals.sort()
		return "{"+",".join([str(e) for e in self.vals])+ " }"
c = IntSet()
c.insert(3)
c.insert(4)
c.insert(40)

print c

c.remove(3)

print c

print c.member(3)

