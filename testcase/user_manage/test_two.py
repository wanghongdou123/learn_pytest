import pytest


from common.common_util import CommonUtil
from common.yaml_util import read_yaml
from common.requests_util import RequestUtil

class TestOne(CommonUtil):



    # @pytest.mark.smoke
    # def test_six(self):
    #     print('test_six')
    #     assert 1==1
    #     assert 'a' in 'apple'


    ACCESS_TOKEN = ''


    @pytest.mark.parametrize('caseinfo', read_yaml('testcase/user_manage/get_token.yml'))
    def test_seven(self,caseinfo):
        # print(caseinfo)
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        validate = caseinfo['validate']

        res = RequestUtil.session.request(method=method,url=url,params=data)
        result = res.json()
        TestOne.ACCESS_TOKEN = result['access_token']
        print(TestOne.ACCESS_TOKEN)



    @pytest.mark.parametrize('caseinfo', read_yaml('testcase/user_manage/edit_flag.yml'))
    def test_eight(self, caseinfo):
        # print(caseinfo)
        name = caseinfo['name']
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']+TestOne.ACCESS_TOKEN
        print(url)
        data = caseinfo['request']['data']
        validate = caseinfo['validate']
        res = RequestUtil.session.request(method=method, url=url, json=data)
        result = res.json()
        print(result)

