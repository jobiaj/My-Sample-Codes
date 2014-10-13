def gen_prime():
	for num in range(1,1000):
			for i in range(2,num):
				if ((num%i) == 0):
					break
				else:
					yield num



b = gen_prime()
print b.next()
print b.next()
print b.next()
print b.next()
