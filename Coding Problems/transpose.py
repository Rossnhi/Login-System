def transpose(m):
	t=[]
	r=len(m)
	c=len(m[0])
	for i in range(c):
		t_elements=[]
		for j in range(r):
			t_elements+=[m[j][i]]
		t+=[t_elements]
	return(t)
