# import json
# import os
# import allure
# import pytest
# from common.handle_test import Handle
# from config import Conf
# from utils.YamlUtil import YamlReader
#
# getDataIndexValueTreeList = os.path.join(Conf.get_data_path(), "TITAN_getDataIndexValueTreeList.yml")
# data_index_value_tree_list = YamlReader(getDataIndexValueTreeList).read_data_all()
#
#
# @allure.feature("Titan筛选")
# class TestTitan:
#     @pytest.mark.parametrize("index_value_tree_list", data_index_value_tree_list)
#     def test_data_index_value_tree_list(self, index_value_tree_list):
#         Handle().handle_test(index_value_tree_list)
