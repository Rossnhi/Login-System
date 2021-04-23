def mod(x):
	if x>=0:
		return(x)
	if x<0:
		return(-x)
def sumprimes(l):
	l=list(l)+[4]
	n=len(l)
	positive_list=[]
	for k in range(0,n):#or k in l
		positive_list+=[mod(l[k])]#or positive_list+=[mod(k)]
	m=max(positive_list)
	composites=[]
	one=[1,-1,0]
	for i in range(2,(m+1)):
		for k in range(0,n):#or k in l
			if l[k]%i==0 and l[k]/i!=1:#or k%i==0 and k/i!=1
				composites+=[l[k]]#or composites+=[k]
				primes_with_one=[x for x in l if x not in composites]
				primes=[x for x in primes_with_one if x not in one]
				y=sum(list(primes))
	return(y)	
			


				


