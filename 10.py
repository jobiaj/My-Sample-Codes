
class reverse_iter:
    def __init__(self, n):
        self.n = n
	self.count = len(self.n)
    def __iter__(self):
        return self
    #def reverse1(self):
	#for i in self.n[::-1]:
	#	return i
    def next(self):
      	for i in self.n[::-1]:
        	if self.count>0:
			return i
			self.count = self.count -1
		if (self.count == 0): 
            		raise StopIteratio()

y = reverse_iter([1,2,3,4,5])
print y.next()
print y.next()
print y.next()
for i in y:
	print i
