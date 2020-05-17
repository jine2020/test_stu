from decimal import Decimal

import pytest


class TestCalc():

    @pytest.mark.add
    @pytest.mark.parametrize('a,b',[(1,2)])
    def test_add(self, a, b):
        return a + b

    @pytest.mark.div
    @pytest.mark.parametrize('a,b', [(1, 2)])
    def test_div(self, a, b):
        try:
            return a / b
        except:
            return 'division by zero'

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b', [(1, 2)])
    def test_sub(self, a, b):
        return a - b

    @pytest.mark.mul
    @pytest.mark.parametrize('a,b', [(1, 2)])
    def test_mul(self, a, b):
        return float(Decimal(str(a)) * Decimal(str(b)))

if __name__ == '__main__':
    pytest.main(['-vs'])