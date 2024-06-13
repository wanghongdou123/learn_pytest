import pytest


@pytest.fixture(scope="function",autouse=True,name='login')
def login():
    print('登录成功之前')
    yield '登录成功'
    print('登录成功之后')
