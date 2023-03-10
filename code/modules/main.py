# import wt
# from calc import Calc
# from files import csv_file
import oboyo as g
# from geo.calc import Calc, Distance


def main():

    x = 2
    y = 3

    temp = g.Calc()
    # assert temp.add(x, y) == 5
    # print(g.Calc.add())
    print(temp.add(x, y))
    print(temp.multiply(x, y))
    dist = g.Distance(x)
    print(dist.power(x))

    start = 'hello'
    end = 'world'

    test = g.Wt(start, end)
    print(test.convert_to())
    print(test.convert_from())

    file1 = 'foo.csv'
    file2 = 'fum.xlsx'
    print(g.check(file1))
    print(g.check(file2))
    # get = g.csv_file.check(file1)
    # print(get, 'k')
    # get.check(file2)


main()
