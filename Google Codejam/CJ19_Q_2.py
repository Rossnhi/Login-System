def path(N,P):
	mypath = ""
	mE = 0
	mS = 0
	lE = 0
	lS = 0
	for i in range((2*N)-2):
		if mE + mS == lE + lS:
			if P[i] == "E":
				mypath += "S"
				mS += 1
			else:
				mypath += "E"
				mE += 1
		else:
			if mypath[i-1] == "E":
				mypath += "S"
				mS += 1
			else:
				mypath += "E"
				mE += 1
		if P[i]  == "E":
			lE += 1
		else:
			lS += 1
	return(mypath)
for tc in range(int(input())):
    	N = int(input())   
    	P = input().strip()
    	print( "case #%d: %s" %(tc + 1, path(N, P)))
