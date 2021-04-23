def nofour(n):
	n = str(n)
	A = ""
	B = ""
	for i in range(len(n)):
		if n[i] != "4":
			A += n[i]
			B += '0'
		else:
			A += "2"
			B += "2"
	return((int(A), int(B)))
for tc in range(int(input())):
        n = int(input())
        a, b = nofour(n)
        print( "case #%d: %d %d" %(tc + 1, a, b))
