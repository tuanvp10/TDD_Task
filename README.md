# Python TDD Task

Trying out a TDD approach to writing a calculator

First, we ensure that pytest is installed as we need this to run our tests.

Since we are trialling Test-Driven Development, we write the tests before the code, defining what functions we want to have in our calculator and what we want them to return for our test cases.

To do this, we create a class that inherits from the TestCase class in the unittest library. This class lets us run methods to test the functionality of our code. We also need to have imported the classes we want to test.

After that we simply define what we require the test case to return when we run a function with a set of inputs. Instantiating an object of the testable code in our test case and then defining the functions lets us run the test case to make sure the code does what we want it to. The full code is below:

```python
import pytest
import unittest

from func_calc import FuncCalc

class FuncTest(unittest.TestCase):

    func_calc = FuncCalc()

    def test_cm_to_inch(self):
        self.assertEqual(self.func_calc.cm_to_to_inch(4), 10.16)

    def test_modular(self):
        self.assertEqual(self.func_calc.modular(4, 3), 1)

    def test_triangle_area(self):
        self.assertEqual(self.func_calc.triangle_area(8, 9), 36)

    def test_percentage(self):
        self.assertEqual(self.func_calc.percentage(4, 10), 40)
```

Notice that all testing functions start with test, which is important as it is needed for the interpreter to recognise them as tests. Also notice that the test of divisible has three test cases, one for each branch of the intended control flow.

Now that we have defined what tests we want our code to pass, we write code to pass these tests. As this exercise is about the TDD approach, I imported my funcCalc class:

```python
class FuncCalc:

    def cm_to_to_inch(self, num1):
        return num1 * 2.54

    def modular(self, num1, num2):
        return num1 % num2

    def triangle_area(self, numB, numH):
        return (numB * numH) / 2

    def percentage(self, num1, num2):
        return 100 * (num1 / num2)
```
The results showed all tests were passed.