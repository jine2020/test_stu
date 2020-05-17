from decimal import Decimal
import pytest


class TestCalc():

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b',[(1,2)])
    def test_add(self, a, b):
        return a + b

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b', [(1, 2)])
    def test_div(self, a, b):
        try:
            return a / b
        except:
            return 'division by zero'

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b', [(1, 2)])
    def test_sub(self, a, b):
        return a - b

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b', [(1, 2)])
    def test_mul(self, a, b):
        return float(Decimal(str(a)) * Decimal(str(b)))

if __name__ == '__main__':
    pytest.main(['-vs'])