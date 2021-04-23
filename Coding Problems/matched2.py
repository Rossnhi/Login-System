def matched(s):
	s=list(s)
	n=len(s)
	t=5<6
	f=5>6
	count=0
	for k in s:
		if k=="(":
			count+=1
		if k ==")":
			count-=1
	if count!=0:
		return(f)
	if count==0:		
		i=0
		while i<n:
			if s[i]=="(":
				s.remove(s[i])
				s.remove(")")
				i+=1
			if s[i]==")":
				return(f)
			else:
				i+=1
		return(t)
				


				
			




			    	 
