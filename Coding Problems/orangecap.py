def orangecap(d):
	total_scores={}
	for i in d.keys():
		for j in d[i].keys():
			if j in total_scores:
				total_scores[j]+=d[i][j]
			else:
				total_scores[j]=d[i][j]
	m=max(list(total_scores.values()))
	for k in total_scores.keys():
		if total_scores[k]==m:
			y=(k,m)
	return(y)
			

