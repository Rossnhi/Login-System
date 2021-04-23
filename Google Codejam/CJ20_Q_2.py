def para(s):
	open = 0
	s_ = ""
	for i in s:
		if open <= int(i):
			s_ += (int(i) - open) * "(" + i
			open += (int(i) - open) * 1
		else:
			s_ += (open - int(i)) * ")" + i
			open -= (open - int(i)) * 1
	s_ += open * ")"
	return(s_)

for tc in range(int(input())):
	s = input().strip()	
	print( "case #%d: %s" %(tc + 1, para(s)))	