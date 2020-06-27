import pytest


@pytest.fixture()
def login():
    print('登录')
    username='jine'
    yield username
    print('新建项目')


class TestDemo:
    def setup_class(self):
        print('打开浏览器')

    def teardown_class(self):
        print('关闭浏览器')
    # def setup(self):
    #     print('登录')
    #
    # def teardown(self):
    #     print('退出')

    def test_a(self,login):
        print('testa')
        print(f'{login}')

    def test_b(self):
        print('testb')

    def test_c(self,login):
        print('testc')
        print(f'{login}')