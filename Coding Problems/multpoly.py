def reverse(l):
	if l == []:
		return (l)
	else:
		return (l[-1:] + reverse(l[:-1]))
def multpoly(p1,p2):
	y=[]
	for i in range(len(p1)):
		for j in range(len(p2)):
			y+=[(p1[i][0]*p2[j][0],p1[i][1]+p2[j][1])]
	copy_y=y[0:len(y)]
	copy_y+=[(y[i][0]+y[j][0],y[i][1]) for i in range(len(y)) for j in range(i+1,len(y)) if y[i][1]==y[j][1]]
	for i in range(len(y)):
		for j in range(i+1,len(y)):
			if y[i][1]==y[j][1]:
				copy_y.remove(y[i])
				copy_y.remove(y[j])
	copy_y2=copy_y[0:len(copy_y)]
	for i in range(len(copy_y)):
		if copy_y[i][0]==0:
			copy_y2.remove(copy_y[i])
	copy_y2.sort(key=lambda x:x[1])
	copy_y2=reverse(copy_y2)
	return(copy_y2)		

				