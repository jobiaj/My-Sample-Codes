def pos_neg(nums):
	x = []
	y = []
	n = len(nums)/2
	for i in nums:
		x.append(0-i)
	#return x
	for j in nums:
		y.append(j)
	
	return x[:n] +  y[n:]
print pos_neg([1,2,3,4,6])
		
        	
