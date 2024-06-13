import pytest
from common.common_util import CommonUtil



class TestOne(CommonUtil):

    @pytest.mark.smoke
    def test_one(self):
        print('test_one')


    @pytest.mark.login
    def test_two(self):
        print('test_two')

    @pytest.mark.shopping
    def test_three(self):
        print('test_three')


    # @pytest.mark.skip(reason = '跳过test_four')
    # def test_four(self):
    #     print('test_four')
    #
    # a = 2
    # @pytest.mark.skipif(a < 5,reason = "太少了")
    # def test_five(self):
    #     print('test_five')
    #



class TestTwo(CommonUtil):

    def test_six(self):
        print('test_six')

