from files import file

class Csv(file.File):

	def __init__(self, file):
		super().__init__(file)
	
	def check(self):
		if self.file.endswith('csv'):
			print('file is csv')
		elif self.file.endswith('xlsx'):
			print('file is xlsx')