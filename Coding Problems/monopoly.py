class monopoly:
	def __init__(self,d):
		self.d=d
	def income(self,x,m):
		self.d[x]+=m
	def revenue(self,x,m):
		self.d[x]-=m
	def trade(self,x,y,m):
		self.revenue(x,m)
		self.income(y,m)

