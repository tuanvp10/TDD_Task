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