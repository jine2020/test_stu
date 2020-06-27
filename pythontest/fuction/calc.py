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
if __name__ == '__main__':
    print(Calc().mul(0.1, 0.1))