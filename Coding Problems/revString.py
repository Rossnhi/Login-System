# def revString(s):
# 	if len(s) == 1:
# 		return(s)
# 	return(revString(s[1:]) + s[0])
# s = "hello"
# print(revString(s))
# print(s)

# def revNum(n):
# 	ans = 0
# 	while(n > 0):
# 		ans *= 10
# 		ans += n%10
# 		n = n//10
# 	return(ans)

# def revNum(n, ans = 0):
# 	if n == 0:
# 		return(ans)
# 	ans *= 10
# 	ans += n%10
# 	n = n//10
# 	return(revNum(n, ans))

# number = 1234567
# print(revNum(number))
# print(number)

def forLoop(n, i = 0, inc = 1):
	#declare all global variables here
	
	if i == n:
		return
	
	#input code here that goes inside for loop
	
	
	i += inc
	return(forLoop(n, i))
forLoop(5)
