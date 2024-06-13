import pytest

def yaml_data():
    return ['one','two']


@pytest.fixture(scope="function",autouse=True,params=yaml_data(),ids=['1','2'],name='db')
def sql_data(request):
    print(request.param)
    # 前置
    print('商品管理之前')
    yield request.param
    # 后置
    print('商品管理之后')