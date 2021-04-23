def insertion_sort_d(l):
	n=len(l)
	for sort_end in range(n):
		pos=sort_end
		while pos>0 and l[pos]>l[pos-1]:
			(l[pos],l[pos-1])=(l[pos-1],l[pos])
			pos-=1
	return(l)		

n = int(input())
buffer = []
for i in range (0,n):
	buffer.append ( input())
#print (buffer) #

pitches = []
for i in range (0,n):
	j = buffer[i].find(" ")
	pitches.append( int( buffer[i][0:j]))
#print (pitches) #

pitches_sort = pitches[:]
insertion_sort_d ( pitches_sort)
#print ( pitches_sort) #

scores = []
for i in range (0,n):
	scores.append( 2*i)
#print (scores) #

scores_str = []
for i in range (0,n):
	j = pitches_sort.index( pitches[i])
	scores_str.append( str( scores[j]))
#print (scores_str) #

final_score = ""
for i in scores_str:
	final_score = final_score + i + " "
print ( final_score)




	











	
