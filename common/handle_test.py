from common.get_report import Report
from utils.Assert import Assertions
from utils.LogUtil import logger
from utils.RequestsUtil import Request


class Handle:
    def handle_test(self, info, data_type="data"):
        case_name = info['case_name']
        logger().debug(case_name)
        url = info['url']
        method = info['method']
        data = info['data']
        logger().debug(data)
        expect = info['expect']
        logger().debug(expect)
        if method == "GET":
            res = Request().get(url, params=data)
        elif method == "POST":
            if data_type == "data":
                res = Request().post(url, data=data)
            elif data_type == "json":
                headers = {"Content-Type": "application/json; charset=UTF-8"}
                res = Request().post(url, json=data, headers=headers)
            else:
                logger().error("data_type 输入有误")
        else:
            logger().error("method 输入有误")
        code = res["code"]
        body = res["body"]
        logger().info(res)
        if isinstance(expect, list):
            for i in range(len(expect)):
                ex = str(expect[i])
                Assertions().assert_in_text(body, ex, case_name, url, method, data)
        else:
            ex = str(expect)
            Assertions().assert_in_text(body, ex, case_name, url, method, data)
        Assertions().assert_code(200, code)
        Report().get_report(case_name, url, method, data, expect, res)

    # 返回请求响应
    def handle_res(self, info, data_type="data"):
        case_name = info['case_name']
        logger().debug(case_name)
        url = info['url']
        method = info['method']
        data = info['data']
        logger().debug(data)
        expect = info['expect']
        logger().debug(expect)
        if method == "GET":
            res = Request().get(url, params=data)
        elif method == "POST":
            if data_type == "data":
                res = Request().post(url, data=data)
            elif data_type == "json":
                headers = {"Content-Type": "application/json; charset=UTF-8"}
                res = Request().post(url, json=data, headers=headers)
            else:
                logger().error("data_type 输入有误")
        else:
            logger().error("method 输入有误")
        return res, case_name, method, expect

    # 返回请求响应
    def handle_res_body(self, info, data_type="data"):
        url = info['url']
        method = info['method']
        data = info['data']
        logger().debug(data)
        if method == "GET":
            res = Request().get(url, params=data)
        elif method == "POST":
            if data_type == "data":
                res = Request().post(url, data=data)
            elif data_type == "json":
                headers = {"Content-Type": "application/json; charset=UTF-8"}
                res = Request().post(url, json=data, headers=headers)
            else:
                logger().error("data_type 输入有误")
        else:
            logger().error("method 输入有误")
        return res["body"]


