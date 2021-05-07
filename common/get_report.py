import allure
from config.Conf import ConfigYaml


class Report:

    def get_report(self, case_name, url, method, data, expect, res):
        # 接口名称  title
        allure.dynamic.title(case_name)
        url = ConfigYaml().get_conf_url() + url
        # 请求URL  请求类型 期望结果 实际结果描述
        desc = "" \
               "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
               "<font color='red'>请求参数: </font>{}<Br/>" \
               "<font color='red'>期望字段: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(url, method, data, expect, res)
        allure.dynamic.description(desc)

    def get_titan_report(self, case_name, url, method, data, expect,):
        # 接口名称  title
        allure.dynamic.title(case_name)
        url = ConfigYaml().get_conf_url() + url
        # 请求URL  请求类型 期望结果 实际结果描述
        desc = "" \
               "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
               "<font color='red'>请求参数: </font>{}<Br/>" \
               "<font color='red'>期望字段: </font>{}<Br/>" .format(url, method, data, expect)
        allure.dynamic.description(desc)
