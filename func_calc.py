# create a new git hub repo and project in pycharm
# create tests for functions cm to inches, modular, Triangle calculation and calculate %.
# write the code to pass all the tests
# create 2 files 1 for tests and 1 for functional code
# apply OOP to achieve the desired results.

class FuncCalc:

    def cm_to_to_inch(self, num1):
        return num1 * 2.54

    def modular(self, num1, num2):
        return num1 % num2

    def triangle_area(self, numB, numH):
        return (numB * numH) / 2

    def percentage(self, num1, num2):
        return 100 * (num1 / num2)