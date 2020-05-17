import pytest,allure,yaml

from test_stu.pythontest.calc import Calc

@allure.feature('计算器')
class TestCalc():
    def setup(self):
        self.calc = Calc()

    @allure.story('两数相加')
    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('data.yml')))
    def test_add(self, a, b, result):
        assert self.calc.add(a, b) == result

    @allure.story('两数相除')
    @pytest.mark.parametrize('a,b,result',
                             [(0, 0, 'division by zero'), (0, 1, 0), (0, -1, 0),
                              (1, 1, 1), (-1, -1, 1), (-99999, -99999, 1),
                              (9999, 9999, 1), (0.1, 0.1, 1),
                              (-0.1, -0.1, 1), (0, -0.1, 0), (0, 0.1, 0),
                              (-99999.1, -99999.1, 1),
                              (9999.1, 9999.1, 1)])
    @allure.step('运算')
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result

    @allure.story('两数相减')
    @pytest.mark.parametrize('a,b,result',
                             [(0, 0, 0), (0, 1, -1), (0, -1, 1), (1, 1, 0), (-1, -1, 0), (-99999, -99999, 0),
                              (9999, 9999, 0), (0.1, 0.1, 0),
                              (-0.1, -0.1, 0), (0, -0.1, 0.1), (0, 0.1, -0.1), (-99999.1, -99999.1, 0),
                              (9999.1, 9999.1, 0)])
    def test_sub(self, a, b, result):
        assert self.calc.sub(a, b) == result

    @allure.story('两数相乘')
    @pytest.mark.parametrize('a,b,result',
                             [(0, 0, 0), (0, 1, 0), (0, -1, 0), (1, 1, 1), (-1, -1,1), (-99999, -99999, 9999800001),
                              (9999, 9999, 99980001), (0.1, 0.1, 0.01),
                              (-0.1, -0.1, 0.01), (0, -0.1, 0), (0, 0.1, 0), (-99999.1, -99999.1,9999820000.81),
                              (9999.1, 9999.1, 99982000.81)])
    def test_mul(self, a, b, result):
        assert self.calc.mul(a, b) == result

if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_add'])
