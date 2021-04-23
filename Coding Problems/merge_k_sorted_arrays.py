def merge_k_arr(L):
	k = len(L)
	output = []
	index = [0] * k
	counter = k
	while(counter > 1):
		l = -1
		max = -1
		for i in range(k):
			if index[i] == -1:
				continue
			if L[i][index[i]] > max:
				max = L[i][index[i]]
				l = i
		output.append(max)
		if index[i] < len(L[i]) - 1:
			index[i] += 1
		else:
			index[i] = -1
			counter -=1
	for i in range(k):
		if index[i] != -1:
			output.append(l[i][index[i] : len[L[i]]])
	return(output)
	
