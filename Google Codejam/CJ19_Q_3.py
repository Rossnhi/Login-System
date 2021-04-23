import math
def decrypt(N,L,cipher):
	alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	primes = [0]* (L+1)
	for i in range(L-1):
		if cipher[i] == cipher[i+1]:
			continue
		primes[i+1] = math.gcd(cipher[i], cipher[i+1])
	for i in range(1, L+1):
		if primes[i] == 0:
			if primes[i-1] != 0:
				primes[i] = cipher[i-1] // primes[i-1]
	for i in range(L-1, -1, -1):
		if primes[i] == 0:
			if primes[i+1] != 0:
				primes[i] = cipher[i] // primes[i+1]
	alphaprimes = sorted(list(set(primes)))
	plaintext = ""
	for i in primes:
		plaintext += alphabets[alphaprimes.index(i)]
	return(plaintext)
for tc in range(int(input())):
		N, L = map(int, input().split())
		cipher = list(map(int, input().split()))
		print( "case #%d: %s" %(tc + 1, decrypt(N, L, cipher))) 
		
		
