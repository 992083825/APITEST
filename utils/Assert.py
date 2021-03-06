"""
封装Assert方法

"""

import json

from common.get_report import Report
from utils.LogUtil import logger


class Assertions:
    def __init__(self):
        self.log = logger()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))

            raise

    def assert_in_text(self, body, expected_msg, case_name=None, url=None, method=None, data=None):
        """
        验证response body中是否包含预期字符串
        :param data:
        :param method:
        :param url:
        :param case_name:
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert expected_msg in text
            return True
        except:
            # self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            self.log.error("期待字段是：%s" % expected_msg)
            self.log.error("实际结果是：%s" % text)
            Report().get_report(case_name, url, method, data, expected_msg, text)
            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))

            raise

    def assert_in_titan_data(self, test_list, standard_list, indicator_name):
        try:
            if set(test_list).difference(set(standard_list)):
                assert False
            else:
                return True
        except:
            diff1 = set(test_list).difference(set(standard_list))
            diff2 = set(standard_list).difference(set(test_list))
            if str(diff1) != "":
                str_diff1 = indicator_name + "病种，16环境比待测试环境多的指标为：" + str(diff1)
            else:
                str_diff1 = indicator_name + "病种，16环境没有比待测试环境多的指标 "
            if str(diff1) != "":
                str_diff2 = indicator_name + "病种，待测试环境比16环境多的指标为：" + str(diff2)
            else:
                str_diff2 = indicator_name + "病种，待测试环境没有比16环境多的指标 "
            self.log.error(str_diff1)
            self.log.error(str_diff2)

            # raise
