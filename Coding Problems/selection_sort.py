def selection_sort_d(l):
	n=len(l)
	for start in range(n):
		max_pos=start
		for i in range(start,n):
			if l[i]>l[max_pos]:
				max_pos=i
		(l[max_pos],l[start])=(l[start],l[max_pos])
	return(l)
def selection_sort_a(l):
	n=len(l)
	for start in range(n):
		min_pos=start
		for i in range(start,n):
			if l[i]<l[min_pos]:
				min_pos=i
		(l[min_pos],l[start])=(l[start],l[min_pos])
	return(l)
			