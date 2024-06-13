import pytest

@pytest.fixture(scope="function",autouse=True,name='um')
def user_manage():
    print('用户管理之前')
    yield 'success'
    print('用户管理之后')