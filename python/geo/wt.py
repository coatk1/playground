class Wt:

	def __init__(self, to, fro):
		self.to = to
		self.fro = fro

	def convert_to(self):
		return self.to
	
	def convert_from(self):
		return self.fro
		
class Gh:

	def __init__(self, gh, la, lo):
		self.gh = gh
		self.la = la
		self.lo = lo
	