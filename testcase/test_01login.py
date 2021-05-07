import os

import allure
import pytest
import requests
from ruamel import yaml
from common.get_report import Report
from config import Conf
from config.Conf import ConfigYaml
from utils.Assert import Assertions
from utils.RequestsUtil import Request
from utils.YamlUtil import YamlReader

user_list = list()
user_info = ConfigYaml().get_user_info()
user_list.append(user_info)

depa_info = os.path.join(Conf.get_data_path(), "get_hospital_department.yml")
dep_info = YamlReader(depa_info).read_list_data()


@allure.feature("登录")
class TestLogin:
    @pytest.mark.parametrize("login", user_list)
    @allure.title("登录接口")
    def test_login(self, login):
        url = ConfigYaml().get_conf_url() + login["url"]
        data = login["data"]
        userName = login["data"]["userName"]
        s = requests.post(url, data=data)
        # 返回状态码
        Assertions().assert_code(s.status_code, 200)
        # 返回结果内容
        Assertions().assert_in_text(s.text, userName)
        global SSO_COOKIE, JSESSIONID, uniqu_no, authUserId, authName, access_token
        SSO_COOKIE = s.cookies['SSO_COOKIE']
        JSESSIONID = s.cookies['JSESSIONID']
        uniqu_no = s.json()["data"]["uniquNo"]
        authUserId = s.json()["data"]["userId"]
        authName = s.json()["data"]["realName"]
        access_token = s.json()["data"]["accessToken"]

    @pytest.mark.parametrize("info", dep_info)
    def test_info(self, info):
        self.case_name = info['case_name']
        self.url = info['url']
        self.method = info['method']
        self.data = info['data']
        info['data']['id'] = authUserId
        self.expect = info['expect']
        res = Request().get(self.url, params=self.data)
        body = res["body"]
        Assertions().assert_in_text(body, self.expect)
        Report().get_report(self.case_name, self.url, self.method, self.data, self.expect, res)
        if Assertions().assert_in_text(body, self.expect):
            data = dict()
            login = {"SSO_COOKIE": SSO_COOKIE, "JSESSIONID": JSESSIONID, "uniqu_no": uniqu_no, "authUserId": authUserId,
                     "operatorId": authUserId, "userId": authUserId, "authName": authName, "access_token": access_token,
                     "authToken": access_token, "orgName": body["data"]["roleList"][0]["orgName"],
                     "roleName": body["data"]["roleList"][0]["roleName"],
                     "hospitalCode": body["data"]["topOrg"]["code"]}
            data["login"] = login

            file = Conf.get_config_login()
            with open(file, "w", encoding="utf-8") as f:
                yaml.dump(data, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)


if __name__ == "__main__":
    pytest.main(["-s", "Test_login.py"])
