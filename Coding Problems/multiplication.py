def multiplication(m,n):
	if n==1:
		return(m)
	y=m+multiplication(m,n-1)
	return(y)
		