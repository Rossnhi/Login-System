def mod(s):
	if s>=0:
		return(s)
	if s<0:
		return(-s)
def factors(x):
	factors=[]
	for i in range(2,mod(x)):
		if x%i==0 and x//i>0:
			factors+=[i]
	return(factors)
	
def sumprime(l):
	primes=[]
	for k in l:
		if len(factors(k))==0 or len(factors(k))==1:
			primes+=[k]
	y=sum(primes)		
	return(y)
