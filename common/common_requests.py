import requests
from requests.adapters import HTTPAdapter
from common.yamlconfig import GetConf
from common.deal_with_response import del_with_response


class Requests:
    def __init__(self, headers=None, timeout=10):
        """
        requests封装
        :param headers:
        :param timeout:
        """
        self.s = requests.Session()
        # 在session实例上挂载adapter实例，m目的是请求异常时，自动重试
        self.s.mount("http://", HTTPAdapter(max_retries=3))
        self.s.mount("https://", HTTPAdapter(max_retries=3))
        # 公共的请求头设置
        self.s.headers = headers
        self.timeout = timeout
        self.url = GetConf().geturl()

    def get(self, url, params=None):
        res = self.s.get(self.url + url, params=params, timeout=self.timeout)
        del_with_response(params, res)
        return res

    def post(self, url, data=None, json=None):
        if data:
            res = self.s.post(self.url + url, data=data, timeout=self.timeout)
            del_with_response(data, res)
            return res
        if json:
            res = self.s.post(self.url + url, json=json, timeout=self.timeout)
            del_with_response(json, res)
            return res

        res = self.s.post(self.url + url, timeout=self.timeout)
        del_with_response(json, res)
        return res

    def __del__(self):
        """
        当实例被销毁时，释放session所持有的连接
        """
        if self.s:
            self.s.close()
