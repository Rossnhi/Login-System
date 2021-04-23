# https://codeforces.com/contest/1328/problem/F
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a_cnt = []
cuml_cnt = []
cumg_cnt = []
cuml = 0
count = 1
res = -1
for i in range(1,n):
	if count == k:
		res = 0
		break
	if a[i] == a[i-1]:
		count += 1
	else:
		a_cnt.append([a[i-1], count])
		cuml += count
		cuml_cnt.append(cuml)
		for j in range(len(cumg_cnt)): # doesn't work with "for j in cumg_cnt" 
			cumg_cnt[j] += count
		cumg_cnt.append(count)
		count = 1
	if i == n-1:
		a_cnt.append([a[i], count])
		cuml += count
		cuml_cnt.append(cuml)
		for j in range(len(cumg_cnt)):
			cumg_cnt[j] += count
		cumg_cnt.append(count)
if res != 0:
	def fl(i): # number of moves it takes to make all elements less than i into i
		if i == 0:
			return(0)
		return( fl(i-1) + ((a_cnt[i][0] - a_cnt[i-1][0]) * cuml_cnt[i-1]))
	def fg(i): # number of moves it takes to make all elements greater than i into i
		if i == len(a_cnt)-1:
			return(0)
		return( fg(i+1) + ((a_cnt[i+1][0] - a_cnt[i][0]) *cumg_cnt[i+1]))
	moves = []
	moves.append(fg(1) + ((k - a_cnt[0][1]) * (a_cnt[1][0] - a_cnt[0][0])))
	for i in range(1, len(a_cnt) - 1):
		if (fl(i-1) + (a_cnt[i][0] - a_cnt[i-1][0]) <= (fg(i+1) + a_cnt[i+1][0] - a_cnt[i][0])):
			mn = "l"
		else:
			mn = "g"
		if mn == "l":
			x = fl(i-1) + (min(cuml_cnt[i-1], (k - a_cnt[i][1])) * (a_cnt[i][0] - a_cnt[i-1][0])) 
			if (k - a_cnt[i][1] - min(cuml_cnt[i-1], k - a_cnt[i][1])) != 0:
				x += fg(i+1) + ((k - a_cnt[i][1] - min(cuml_cnt[i-1], k - a_cnt[i][1])) * (a_cnt[i+1][0] - a_cnt[i][0]))
		else:
			x = fg(i+1) + (min(cumg_cnt[i+1], (k - a_cnt[i][1])) * (a_cnt[i+1][0] - a_cnt[i][0])) 
			if (k - a_cnt[i][1] - min(cumg_cnt[i+1], k - a_cnt[i][1])) != 0:
				x += fl(i-1) + ((k - a_cnt[i][1] - min(cumg_cnt[i+1], k - a_cnt[i][1])) * (a_cnt[i][0] - a_cnt[i-1][0]))	
		moves.append(x)
	moves.append(fl(len(a_cnt)-2) + ((k - a_cnt[len(a_cnt)-1][1]) * (a_cnt[len(a_cnt)-1][0] - a_cnt[len(a_cnt)-2][0])))
	res = moves[0]
	for j in moves:
		if j < res:
			res = j
print(res)
