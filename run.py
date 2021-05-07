import os
import subprocess
import pytest
from config import Conf

report_path = Conf.get_report_path() + os.sep + "result"
report_html_path = Conf.get_report_path() + os.sep + "html"

if __name__ == "__main__":
    # 生成测试报告
    pytest.main(["-s", "-q", "--alluredir", report_path])
    # 将测试报告转为html格式
    cmd = "allure generate " + report_path + " -o " + report_html_path + " --clean"
    subprocess.call(cmd, shell=True)
    # '''allure open -h 127.0.0.1 -p 8083 ./Test/allure-result/html'''
    # cmd2 = "allure open -h 127.0.0.1 -p 8083" + report_html_path
    # subprocess.call(cmd2, shell=True)
