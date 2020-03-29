import wt
import calc
from files import csv_file

def main():

	x = 2
	y = 3

	temp = calc.Calc(x, y)
	print(temp.add())
	print(temp.multiply())
	dist = calc.Distance(x)
	print(dist.power())
	
	start = 'hello'
	end = 'world'
	
	test = wt.Wt(start, end)
	print(test.convert_to())
	print(test.convert_from())
	
	file1 = 'foo.csv'
	file2 = 'fum.xlsx'
	get = csv_file.Csv(file1)
	get.check()
	#get.check(file2)


main()