# def triplet(n):
# 	counter = 0
# 	a = 3
# 	while(counter < n):
# 		if ( a%2 == 1):
# 			b = int((a**2/2)-0.5)
# 			c = int((a**2/2)+0.5)
# 		else:
# 			b =	int(((a/2)**2) - 1)
# 			c = int(((a/2)**2) + 1)
# 		if( a < b and b < c):
# 			print(a,b,c)
# 			counter += 1
# 		a += 1
import math
def triplet(n):
	counter = 0
	a = 3
	flag = 0
	while(counter < n):
		b = a + 1
		while(flag == 0):
			c = math.sqrt(b**2 + a**2)
			if(c - int(c) == 0):
				c = int(c)
				print(a,b,c)
				counter += 1
				flag = 1
			b += 1
		a += 1

triplet()