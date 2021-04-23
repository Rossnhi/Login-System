def insertion_sort_d(l):
	n=len(l)
	for sort_end in range(n):
		pos=sort_end
		while pos>0 and l[pos]>l[pos-1]:
			(l[pos],l[pos-1])=(l[pos-1],l[pos])
			pos-=1
	return(l)
def descending(l):
	n=len(l)
	x=l[0:n]
	insertion_sort_d(x)
	if l==x:
		return(5<6)
	else:
		return(5>6)




