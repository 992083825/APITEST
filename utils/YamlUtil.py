import os
import yaml


# 1、创建类
from config import Conf


class YamlReader:
    # 2、初始化，文件是否存在
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None
        self.data = None

        self.rlist = None

    # 3、yaml读取
    # 单个及多个文档读取
    def read_data(self):
        # 第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, "r", encoding="utf-8") as f:
                self._data = yaml.safe_load(f)
        return self._data

    def read_data_all(self):
        if not self._data_all:
            with open(self.yamlf, "r", encoding="utf-8") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return self._data_all

    # 单个文档读取,返回列表
    def read_list_data(self):
        self.data = self.read_data()
        self.rlist = [self.data]
        return self.rlist


if __name__ == '__main__':
    get_patient_list = os.path.join(Conf.get_data_path(), "AKSO_getPatientList.yml")
    patient_list = YamlReader(get_patient_list).read_data_all()
    print(patient_list)
