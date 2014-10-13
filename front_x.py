def front_x(words):
	x = []
	y = []
	for i in words:
		if i.startswith('x'):
			x.append(i)
			x.sort()
		else:
			y.append(i)
			y.sort()
	return x+y

print front_x(['mix','xyz','apple','xanadu','aardvark'])
