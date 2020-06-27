from time import sleep
import pytest

@pytest.fixture(params=[1,2,3,4,5])
def data(request):
    return request.param

def test_not_2(data):
    sleep(1)
    print(f"测试数据{data}")
    assert data<9
def test_not_3(data):
    sleep(1)
    print(f"测试数据{data}")
    assert data<8
def test_not_4(data):
    sleep(1)
    print(f"测试数据{data}")
    assert data<7
def test_not_5(data):
    sleep(1)
    print(f"测试数据{data}")
    assert data<6
def test_not_6(data):
    sleep(1)
    print(f"测试数据{data}")
    assert data<5
if __name__ == '__main__':
    pytest.main('')

#pytest -n auto 可以并发运行测试用例，有多少cpu 并发多少
#pytest -n  4  并发为4
#测试报告 1.pytest --alluredir=./report 2.allure seuve ./report