class PerfectCal(Calculator):
	def modulo(self):
		result = self.first % self.second
		return result   

a = PerfectCal(4, 2)

print(a.modulo())