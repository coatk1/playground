#from files import file

#class Csv(file.File):

#	def __init__(self, file):
#		super().__init__(file)
	
def check(file):
	if file.endswith('csv'):
		print('file is csv')
	elif file.endswith('xlsx'):
		print('file is xlsx')
	else:
		print('no file')