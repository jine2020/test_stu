import unittest
from test_stu.pythontest.fuction.calc import Calc


class TestCal(unittest.TestCase):
    def test_add1(self):
        self.calc = Calc()
        result=self.calc.add(1,2)
        print(result)
        self.assertEqual(3,result)


