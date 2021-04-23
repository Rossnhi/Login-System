def q(m,n):
	if m<n:
		(m,n)=(n,m)

	q=0
	while m> 0: #or m-n>=0
		(q,m) = (q+1,m-n)
	return(q)
