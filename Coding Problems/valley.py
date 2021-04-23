def insertion_sort_d(l):
	n=len(l)
	for sort_end in range(n):
		pos=sort_end
		while pos>0 and l[pos]>l[pos-1]:
			(l[pos],l[pos-1])=(l[pos-1],l[pos])
			pos-=1
	return(l)
def strict_descending(l):
	n=len(l)
	if n==0 or n==1:
		return(5>6)
	x=l[0:n]
	insertion_sort_d(x)
	if l==x:
		return(5<6)
	else:
		return(5>6)
def insertion_sort_a(l):
	n=len(l)
	for sort_end in range(n):
		pos=sort_end
		while pos>0 and l[pos]<l[pos-1]:
			(l[pos],l[pos-1])=(l[pos-1],l[pos])
			pos-=1
	return(l)
def strict_ascending(l):
	n=len(l)
	if n==1 or n==0:
		return(5>6)
	x=l[0:n]
	insertion_sort_a(x)
	if l==x:
		return(5<6)
	else:
		return(5>6)
def valley(l):
	n=len(l)
	for j in range(0,n-1):
		if l[j]==l[j+1]:# not l[j]==l[j-1] as at j=0, condition becomes- l[0]==l[-1]. For l=[3,2,1,2,3], l[0]=3=l[-1]. Hence it will return false.
			return(5>6)
	for i in range(0,n):
		if strict_descending(l[0:i+1]) and strict_ascending(l[i:n]):
			return(5<6)
	return(5>6)	
