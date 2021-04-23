def matMul(m1, m2):
	if m1 == [] or m2 == []:
		return([])
	try:
		ans = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
		for i in range(len(ans)):
			for j in range(len(ans[0])):
				ans[i][j] = 0
				for _ in range(len(m1[i])):
					ans[i][j] += m1[i][_] * m2[_][j]
		return(ans)
	except IndexError:
		print("Multiplication is not a valid operation for the entered matrices.")