def reverse(l):
	if l == []:
		return (l)
	else:
		return (l[-1:] + reverse(l[:-1]))
def addpoly(p1,p2):
	y=[]
	copy_p1=p1[0:len(p1)]
	copy_p2=p2[0:len(p2)]
	for i in range(len(p1)):
		for j in range(len(p2)):
			if p1[i][1]==p2[j][1]:
				y+=[(p1[i][0]+p2[j][0],p1[i][1])]
				copy_p1.remove(p1[i])
				copy_p2.remove(p2[j])
	p3=y+copy_p1+copy_p2
	copy_p3=p3[0:len(p3)]
	for i in range(len(p3)):
		if p3[i][0]==0:
			copy_p3.remove(p3[i])
	copy_p3.sort(key=lambda x:x[1])
	copy_p3=reverse(copy_p3)		
	return(copy_p3)				


