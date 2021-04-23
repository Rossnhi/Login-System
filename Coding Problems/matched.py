def matched(s):
	count=0
	for i in s:
		if i=="(":
			count+=1
		if i==")":
			count-=1
		if count<0:
			return(5>6)
	if count==0:
		return(5<6)	
	else:
		return(5>6)






			



			






					
