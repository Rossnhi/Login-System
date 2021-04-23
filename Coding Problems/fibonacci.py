def fibonacci(n):
	if n==1 or n==2:
		return(1)
	y=fibonacci(n-1)+fibonacci(n-2)
	return(y)
