def para(N, activities):
	s_act = activities[0:N]
	s_act.sort(key = lambda x: x[0])
	
	res = []
	cameron = "free"
	jamie = "free"
	for i in s_act:
		if i[0]==i[1]:
			continue
		if cameron != "free":
			if cameron <= i[0]:
				cameron = "free"
		if jamie != "free":
			if jamie <= i[0]:
				jamie = "free"

		if cameron == "free":
			res.append("C")
			cameron = i[1]
			
			
		elif jamie == "free":
			res.append("J")
			jamie = i[1]
		else:
			return("IMPOSSIBLE")
	s = ""
	if res != []:
		for i in activities:
			s += res[s_act.index(i)]
			s_act[s_act.index(i)] = 0 # when two activities share the same time slot
			                          # we will have to remove the 1st activity after processing it
			                          # index() will return only the position of the 1st activity
			                          # whilst not changing the posting of the 2nd or other activities
			                          # hence we don't pop it and instead make it 0 once it's been seen

	return(s)

for tc in range(int(input())):
	N = int(input())
	activities = []
	for i in range(N):
		activities.append(list(map(int,input().split())))
	print( "case #%d: %s" %(tc + 1, para(N, activities)))	