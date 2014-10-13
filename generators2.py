def genFib():
	fib_1 = 1
	fib_2 = 0
	while True:
		next = fib_1 + fib_2
		yield next
		fib_2 = fib_1
		fib_1 = next 

print genFib()
a = genFib()
print a.next()
print a.next()
print a.next()
print a.next()
#for i in a:
#	print i
