class stack:
	def __init__(self, list = []):
		self.show = list
	def push(self,x):
		self.show.append(x)
		return(self.show)
	def pop(self,x):
		self.show.pop(x)
		return(self.show)
	def peek(self):
		return(self.show[-1])
	def delete(self):
		self.show = none
	

