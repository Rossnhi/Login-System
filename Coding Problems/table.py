class table:
	def __init__(self, r, c):
		self.r = r
		self.c = c
		self.t = []
		for i in range(0,r):
			temp =[]
			for j in range(0,c):
				temp.append(0)
			self.t.append(temp)
		for i in self.t:
			print(i)
	def show_table(self):
		for i in self.t:
			print(i)
	def cell(self,x,y,a):
		if x > self.r or y > self.c:
			print( "Enter a cell address within the range of a " + str(self.r) + "x" + str(self.c) + " table")
		else:
			self.t[x-1][y-1] = a
			for i in self.t:
				print(i)
	def row(self, x, l):
		if len(l) != self.c:
			print( "Enter a row of length " + str(self.c) + " only")
		else:
			self.t[x-1] = l
			for i in self.t:
				print(i)
	def column(self, y, l):
		if len(l) != self.r:
			print( "Enter a row of length " + str(self.r) + " only")
		else:
			for i in range(0,self.r):
				self.t[i][y-1] = l[i]
			for i in self.t:
				print(i)
	def add_row(self, l, r = 0):
		



				






		
		
