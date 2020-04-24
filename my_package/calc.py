"""Calculations module."""

'''
import calc
temp = calc.Calc(2, 3)
temp.add()
'''
# Let calc be module instead


class Calc:

    # Constructor
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


class Distance(Calc):

    def __init__(self, x):
        super().__init__(x, x)

    @staticmethod
    def power(x):
        return x ** 2
