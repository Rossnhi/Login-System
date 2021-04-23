def transpose(m):
	r=len(m)
	c=len(m[0])
	t=[]
	for j in range(c):
		t[j]=[]
		for i in range(r):
			t[j]+=m[i][j]
	return(t)
			
