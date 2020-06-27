import pytest, allure, yaml
from decimal import Decimal
class Calc():
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        try:
            return a / b
        except:
            return 'division by zero'

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return float(Decimal(str(a)) * Decimal(str(b)))


@allure.feature('计算器')
class TestCalc():
    def setup(self):
        self.calc = Calc()

    @pytest.mark.add
    @allure.story('两数相加')
    @pytest.mark.parametrize('a,b,result',
                             yaml.safe_load(open('../data.yml'))['add'])
    def test_add(self, a, b, result):
        assert self.calc.add(a, b) == result

    @allure.story('两数相除')
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../data.yml'))['div'])
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
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../data.yml'))['mul'])
    def test_mul(self, a, b, result):
        assert self.calc.mul(a, b) == result

    @allure.story('两数相乘')
    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../data.yml'))['mul'])
    def test_mul1(self, a, b, result):
        assert self.calc.mul(a, b) == result

    def steps(self):
        with open('../data.yml') as f:
            return yaml.safe_load(f)['fangfa']

    @pytest.mark.parametrize('a,b,result', yaml.safe_load(open('../data.yml'))['mul'])
    def test_steps(self, a, b, result):
        steps1 = self.steps()
        for step in steps1:
            if 'mul' == step:
                results = self.calc.mul(a, b)
                print(f'mul result==={results}')
            elif 'mul1' == step:
                results = self.calc.mul(a, b)
                print(f'mul1 result==={results}')
            assert result == results


if __name__ == '__main__':
    pytest.main(['-vs', '-k' 'test_pytest1.py::TestCalc::test_add'])
