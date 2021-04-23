def f(n,m):
	trace = 0
	rows = 0
	cols = 0
	for i in range(n):
		trace += m[i][i]
	visitedc = []
	for i in range(n):
		visitedc.append([])
	repcol = []
	reprow = []
	for i in range(n):
		visitedr = []
		for j in range(n):
			if m[i][j] in visitedr and i not in reprow:
				rows += 1
				reprow.append(i)
			else:
				visitedr.append(m[i][j])
			
			if m[i][j] in visitedc[j] and j not in repcol:
				cols += 1
				repcol.append(j)
			else:
				visitedc[j].append(m[i][j])
	return(trace, rows, cols)

for tc in range(int(input())):
	n = int(input())
	m = []
	for i in range(n):
		m.append(list(map(int,input().split())))
	k, r, c = f(n,m)	
	print( "case #%d: %d %d %d" %(tc + 1, k, r, c) )		