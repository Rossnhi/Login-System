#CJ19_1A_1
def valid_move(x1, y1, x2, y2):
	if (x1 == x2) or (y1 == y2) or (y2-y1 == x2 - x1) or (y2 - y1 == x1 - x2):
		return(False)
	return(True)

def next_move(visited, x, y, backtrack):
	for i in range(len(visited)):
		brflag = 0
		for j in range(len(visited[0])):
			if (visited[i][j] == 0) and (valid_move(x, y, i, j)) and ([i,j] not in backtrack[x][y]):
				brflag = 1
				break
		if brflag == 1:
			return([i,j])
	if brflag == 0:
		return(-1)		

def solve(R, C):
	backtrack = [[[] for x in range(C)] for x in range(R)]
	if (min(R,C) == 2 and max(R,C) < 5) or (min(R,C) == 3 and max(R,C) < 4):
		return("IMPOSIIBLE")
	
	visited = [[0 for x in range(C)] for x in range(R)]
	ans = [[0,0]]
	moves = 1
	visited[0][0] = moves
	x, y = [0,0]  #current cell
	while (moves < R*C):
		print("sol", moves, ans, x, y, visited)
		if next_move(visited, x, y, backtrack) != -1:
			x, y = next_move(visited, x, y, backtrack)
			moves += 1
			visited[x][y] = moves
			ans.append([x,y])
		else:
			brflag = 0
			while moves > 1:
				if next_move(visited, x, y, backtrack) != -1:
					print(x,y,"\n")
					x, y = next_move(visited, x, y, backtrack)
					moves += 1
					visited[x][y] = moves
					for i in visited:
						for j in range(len(i)):
							if i[j] == "B":
								i[j] = 0
					ans.append([x,y])
					print("bt",moves, ans, x, y, visited)
					brflag = 1
					break
				else:
					moves -= 1
					ans.pop()
					backtrack[ans[moves - 1][0]][ans[moves - 1][1]].append([x,y])
					x = ans[moves - 1][0]
					y = ans[moves - 1][1]
			if brflag == 0:
				return("IMPOSSIBLE")
				
				
	for i in range(len(ans)):
		ans[i] = list(map(str, ans[i]))
		ans[i] = " ".join(ans[i])
	ans = "\n".join(ans)
	return(ans)

for tc in range(int(input())):
	R, C = map(int, input().split())
	print("case #%d: %s" %( tc + 1, solve(R,C)))	