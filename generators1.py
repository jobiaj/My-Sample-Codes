def gen_test():
	yield 1
	yield 2
print gen_test()
a = gen_test()
print a.next()
print a.next()
print a.next()
