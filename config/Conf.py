import os
from utils.YamlUtil import YamlReader

# 1、获取项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)

# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"

# 定义data目录的路径
_data_path = BASE_DIR + os.sep + "data"

# 定义report目录的路径
_report_path = BASE_DIR + os.sep + "report"

# 定义天塔规范指标的路径
_titan_indicator_path = BASE_DIR + os.sep + "titan_standard_indicator"

# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + "conf.yml"
# 定义login.yml文件的路径
_config_login = _config_path + os.sep + "login.yml"
# 定义db_conf.yml路径
_db_config_file = _config_path + os.sep + "db_conf.yml"
# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"


def get_report_path():
    """
    获取report绝对路径
    :return:
    """
    return _report_path


def get_titan_indicator_path():
    """
    获取天塔规范指标的绝对路径
    :return:
    """
    return _titan_indicator_path


def get_data_path():
    return _data_path


def get_db_config_file():
    return _db_config_file


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def get_config_login():
    return _config_login


def get_log_path():
    """
    获取Log文件路径
    :return:
    """
    return _log_path


# 2、读取配置文件
# 创建类
class ConfigYaml:

    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).read_data()
        self.db_config = YamlReader(get_db_config_file()).read_data()
        self.login_config = YamlReader(get_config_login()).read_data()

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]

    def get_db_conf_info(self, db_alias):
        """
        根据db_alias获取该名称下的数据库信息
        :param db_alias:
        :return:
        """
        return self.db_config[db_alias]

    def get_user_info(self):
        """
        获取用户配置相关信息
        :return:
        """
        return self.config["login"]

    def get_titan_info(self):
        """
        获取用户配置相关信息
        :return:
        """
        return self.config["titan"]

    def get_login_info(self):
        """
        获取用户配置相关信息
        :return:
        """
        return self.login_config["login"]

    def get_email_info(self):
        """
        获取邮件配置相关信息
        :return:
        """
        return self.config["email"]


if __name__ == "__main__":
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info("db_1"))
    # print(conf_read.get_db_conf_info("db_2"))
    # print(conf_read.get_db_conf_info("db_3"))
    # 1、初始化数据库信息，Base.py init_db
    # print(conf_read.get_email_info())
    print(conf_read.get_user_info())
    print(_config_file)
