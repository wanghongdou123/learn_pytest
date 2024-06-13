import requests

class RequestUtil:
    session = requests.session()


    # 封装请求
    def send_request(self,**kwargs):
        res = RequestUtil.session.request(**kwargs)
        print(res.text)
        return res





