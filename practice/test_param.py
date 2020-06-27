import pytest

test_data_user=["jine",'moke','soso']
@pytest.fixture(scope='module')
def login(request):
    user=request.param
    print(f"登录用户{user}")
    return user

@pytest.mark.parametrize('login',test_data_user,indirect=True)
def test_login(login):
    a=login
    print(f"test_login中的{a}")
    assert a!=''

