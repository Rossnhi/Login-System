def insertion_sort_a(l):
	n=len(l)
	for sort_end in range(n):
		pos=sort_end
		while pos>0 and l[pos]<l[pos-1]:
			(l[pos],l[pos-1])=(l[pos-1],l[pos])
			pos-=1
	return(l)		
def insertion_sort_d(l):
	n=len(l)
	for sort_end in range(n):
		pos=sort_end
		while pos>0 and l[pos]>l[pos-1]:
			(l[pos],l[pos-1])=(l[pos-1],l[pos])
			pos-=1
	return(l)		

