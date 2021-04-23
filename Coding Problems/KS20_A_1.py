def maxbuy(N, B, A):
        max = 0
        A.sort()
        for i in A:
            B -= i
            if B >= 0:
                max += 1
            else:
                break
        return(max)
for tc in range( int(input())):
        N, B = map( int, input().strip().split())
        A = list(map( int, input().strip().split()))
        print( "case #%d: %d" %(tc + 1, maxbuy(N, B, A)))

