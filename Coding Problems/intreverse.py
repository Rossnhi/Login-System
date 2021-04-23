def intreverse(n):
	n=str(int(n))
	x=len(n)
	reverse=str()
	for i in range(0,x):
		reverse=reverse+n[x-1-i]
		y=int(reverse)
	return(y)
	