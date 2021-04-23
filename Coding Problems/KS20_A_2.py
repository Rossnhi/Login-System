def maxbeau(plates, N, K, P):
	max = 0
	while ( P > 0):










for tc in range( int(input())):
        N, k, P = map( int, input().strip().split())
        plates = []
        for i in range(N):
        	plates.append(list(map( int, input().strip().split())))
        print( "case #%d: %d" %(tc + 1, maxbeau(plates, N, K, P)))