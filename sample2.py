def pos_neg(a):

	flag=1;
	for i in range(len(a)):
		if(flag==1):
			a[i]=a[i]*(-1)
		if((i+1)%2==0):
			flag=flag*(-1)
	return a

print pos_neg([1,2,3,4,5,6])
