import requests
import pytest
import re
from common.requests_util import RequestUtil
from common.yaml_util import read_yaml_testcase

class TestApi:

    access_token = ''
    csrf_token = ''
    # session = requests.session()

    # 鉴权接口
    @pytest.mark.parametrize('caseinfo', read_yaml_testcase('testapi.yml'))
    def test_get_token(self,caseinfo):

        print(caseinfo['request']['url'])
        print(caseinfo['request']['params'])

        # url = caseinfo['request']['url']
        # params = {
        #     'grant_type':caseinfo['request']['params']['grant_type'],
        #     'appid':caseinfo['request']['params']['appid'],
        #     'secret':caseinfo['request']['params']['secret']
        # }
        # res = RequestUtil.session.request(method=caseinfo['request']['method'],url=url,params=params)
        # # res = TestApi.session.request('get',url=url,params=params)
        # # res = requests.get(url=url,params=params)
        # # print(res.json())
        # TestApi.access_token = res.json()['access_token']



    # 查询标签接口
    def test_select_flag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/get'
        params = {
            'access_token':TestApi.access_token

        }
        res = RequestUtil.session.request(method='get', url=url, params=params)
        # print(res.json())



    # 编辑标签接口
    def test_edit_flag(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/updata?access_token='+TestApi.access_token
        data = {"tag":{"id":134,"name":"李四"}}
        res = RequestUtil.session.request(method='post', url=url, json=data)
        # res = requests.post(url=url,json=data)
        # print(res.json())



    # 文件上传接口
    def test_file_upload(self):
        url = 'https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=' + TestApi.access_token
        data = {"media":open('/Users/wanghongdou/Desktop/1的副本.jpg','rb')}
        res = RequestUtil.session.request(method='post', url=url, files=data)
        # res = requests.post(url=url, files=data)
        # print(res.json())


    # 访问首页接口
    def test_phpwind(self):
        url = 'http://47.107.116.139/phpwind/'
        res = RequestUtil.session.request(method='get',url=url)
        # res = requests.get(url=url)
        # print(res.text)
        TestApi.csrf_token = re.search('name="csrf_token" value="(.*?)"',res.text).group(1)
        # print(TestApi.csrf_token)


    # 登录接口
    def test_login(self):
        url = 'http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun'
        headers = {
            "Accept": "application/json, text/javascript",
            "X-Requested-With": "XMLHTTPREQUEST"
        }

        data = {
            "username":"baili",
            "password":"baili123",
            "csrf_token": TestApi.csrf_token,
            "backurl":"http://47.107.116.139/phpwind/",
            "invite":""
        }
        res = RequestUtil.session.request(method='post', url=url,headers=headers,data=data)
        # res = requests.post(url=url,headers=headers,data=data)
        # print(res.json())



if __name__ == '__main__':
    TestApi.test_get_token()
    TestApi.test_select_flag()
    TestApi.test_edit_flag()
    TestApi.test_file_upload()
    TestApi.test_phpwind()
    TestApi.test_login()