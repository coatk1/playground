'''
import calc
temp = calc.Calc(2, 3)
temp.add()
'''

class Calc:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self):
		return self.x + self.y
	
	def multiply(self):
		return self.x * self.y
		
class Distance(Calc):

	def __init__(self, x):
		super().__init__(x, x)
		
	def power(self):
		return self.x ** 2