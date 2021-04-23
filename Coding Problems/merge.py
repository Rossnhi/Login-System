def merge_a(l1,l2):
	(y,n,m)=([],len(l1),len(l2))
	(i,j)=(0,0)
	while i+j<m+n:
		if i==n:
			y.append(l2[j])
			j+=1
		elif j==m:
			y.append(l1[i])
			i+=1
		elif l1[i]<=l2[j]:
			y.append(l1[i])
			i+=1
		elif l1[i]>=l2[j]:
			y.append(l2[j])
			j+=1
	return(y)		
