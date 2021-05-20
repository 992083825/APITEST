
import json
import os
import allure
import pytest
from common.handle_test import Handle
from config import Conf
from config.Conf import ConfigYaml
from utils.Assert import Assertions
from utils.YamlUtil import YamlReader


getDataIndexValueTreeList = os.path.join(Conf.get_data_path(), "TITAN_16getDataIndexValueTreeList.yml")
data_index_value_tree_list = YamlReader(getDataIndexValueTreeList).read_data_all()

data_list = list()
def get_data(second_data):
    a = list()
    if second_data["title"] is None or "title" not in second_data.keys():
        title1 = " "
    else:
        title1 = second_data["title"]
    if "children" in second_data and second_data["children"]:
        for third_data in second_data["children"]:
            return get_data(third_data)
    else:
        a.append(title1)
        b = "--".join(a)
        return data_list.append(b)

def get_indicator_data(response_data):
    conf_indicator_list = ConfigYaml().get_titan_info()
    for indicator_name in conf_indicator_list:
        test_indicator_list = list()
        file = Conf.get_titan_indicator_path() + os.sep + indicator_name + ".txt"
        with open(file, "r", encoding="utf-8") as f:
            standard_indicator_list = eval(f.read())
            for first_data in response_data:
                disease_title = first_data["title"]
                if disease_title == indicator_name:
                    test_indicator_list = get_data(first_data)
                    print(test_indicator_list)
            Assertions().assert_in_titan_data(standard_indicator_list, test_indicator_list, indicator_name)
    # return test_indicator_list, standard_indicator_list





@allure.feature("Titan筛选")
class TestTitan:
    @pytest.mark.parametrize("index_value_tree_list", data_index_value_tree_list)
    def test_data_index_value_tree_list(self, index_value_tree_list):
        body = Handle().handle_res_body(index_value_tree_list)
        response_data = body["responseData"]
        # test_indicator_list, standard_indicator_list = get_indicator_data(response_data)
        get_indicator_data(response_data)
        # print(test_indicator_list)
        # write_titan_file(test_indicator_list)
        # standard_indicator_list = read_titan_file()
        # Assertions().assert_in_titan_data(test_indicator_list, standard_indicator_list)

