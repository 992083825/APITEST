import requests

from config.Conf import ConfigYaml
from utils.LogUtil import logger


# 重构
# 1、创建类
class Request:

    # 2、定义公共方法
    def __init__(self):
        self.log = logger("Requests")
        # self.log = MyLog()

    def requests_api(self, url, data=None, json=None, params=None, headers=None, cookies=None, method="get"):
        url = ConfigYaml().get_conf_url() + url
        login = ConfigYaml().get_login_info()
        if method == "get":
            if params is not None:
                if "access_token" in params:
                    params["access_token"] = login["access_token"]
                if "authToken" in params:
                    params["authToken"] = login["authToken"]
                if "userId"in params:
                    params["userId"] = login["userId"]
                if "authUserId"in params:
                    params["authUserId"] = login["authUserId"]
                if "operatorId"in params:
                    params["operatorId"] = login["operatorId"]
                if "hospitalCode"in params:
                    params["hospitalCode"] = login["hospitalCode"]
                if "authName"in params:
                    params["authName"] = login["authName"]
                if "uniqu_no"in params:
                    params["uniqu_no"] = login["uniqu_no"]
            # get请求
            self.log.debug("发送get请求")
            r = requests.get(url, params=params, headers=headers, cookies=cookies)
        elif method == "post":
            if data is not None:
                if "access_token" in data:
                    data["access_token"] = login["access_token"]
                if "authToken" in data:
                    data["authToken"] = login["authToken"]
                if "userId" in data:
                    data["userId"] = login["authUserId"]
                if "authUserId" in data:
                    data["authUserId"] = login["authUserId"]
                if "operatorId" in data:
                    data["operatorId"] = login["operatorId"]
                if "hospitalCode" in data:
                    data["hospitalCode"] = login["hospitalCode"]
                if "authName" in data:
                    data["authName"] = login["authName"]
                if "uniqu_no" in data:
                    data["uniqu_no"] = login["uniqu_no"]
            elif json is not None:
                if "access_token" in json:
                    data["access_token"] = login["access_token"]
                if "authToken" in json:
                    data["authToken"] = login["authToken"]
                if "userId" in json:
                    data["userId"] = login["authUserId"]
                if "authUserId" in json:
                    data["authUserId"] = login["authUserId"]
                if "operatorId" in json:
                    data["operatorId"] = login["operatorId"]
                if "hospitalCode" in json:
                    data["hospitalCode"] = login["hospitalCode"]
                if "authName" in json:
                    data["authName"] = login["authName"]
                if "uniqu_no" in json:
                    data["uniqu_no"] = login["uniqu_no"]
            # post请求
            self.log.debug("发送post请求")
            r = requests.post(url, data=data, json=json, headers=headers, cookies=cookies)
        # 2. 重复的内容，复制进来
        # 获取结果内容
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 内容存到字典
        res = dict()
        res["code"] = code
        res["body"] = body
        # 字典返回
        return res

    # 3、重构get/post方法
    # get
    # 1、定义方法
    def get(self, url, **kwargs):
        # 2、定义参数
        # url,json,headers,cookies,method
        # 3、调用公共方法
        return self.requests_api(url, method="get", **kwargs)

    def post(self, url, **kwargs):
        # 2、定义参数
        # url,json,headers,cookies,method
        # 3、调用公共方法
        return self.requests_api(url, method="post", **kwargs)
