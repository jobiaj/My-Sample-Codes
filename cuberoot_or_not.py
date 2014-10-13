x = int(raw_input('enter the integer: '))
ans = 0
while ans**3 < x:
	ans = ans+1
if ans**3 != x:
 	print str(x), ' is not a perfect cube'
else:
	print 'cube root of' , str(x),'is',str(ans) 
