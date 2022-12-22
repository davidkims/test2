class Calculator():
	def __init__(self, first, second):
		self.first = first
		self.second = second
	def add(self):
		result = self.first + self.second
		return result
	def minus(self):
		result = self.first - self.second
		return result	
	def multiple(self):
		result = self.first * self.second
		return result
	def divide(self):
		result = self.first / self.second
		return result