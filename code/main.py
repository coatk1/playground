#import wt
#from calc import Calc
#from files import csv_file
import geo as g
#from geo.calc import Calc, Distance

def main():

	x = 2
	y = 3

	temp = g.Calc(x, y)
	print(temp.add())
	print(temp.multiply())
	dist = g.Distance(x)
	print(dist.power())
	
	start = 'hello'
	end = 'world'
	
	test = g.wt.Wt(start, end)
	print(test.convert_to())
	print(test.convert_from())
	
	file1 = 'foo.csv'
	file2 = 'fum.xlsx'
	print(g.check(file1))
	print(g.check(file2))
	#get = g.csv_file.check(file1)
	#print(get, 'k')
	#get.check(file2)


main()