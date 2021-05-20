import json
import os
import allure
import pytest
from common.handle_test import Handle
from config import Conf
from config.Conf import ConfigYaml
from utils.Assert import Assertions
from utils.YamlUtil import YamlReader


getDataIndexValueTreeList = os.path.join(Conf.get_data_path(), "TITAN_12getDataIndexValueTreeList.yml")
data_index_value_tree_list = YamlReader(getDataIndexValueTreeList).read_data_all()


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
                    if "children" in first_data and first_data["children"]:
                        for second_data in first_data["children"]:
                            if second_data["title"] is None:
                                second_data["title"] = " "
                            primary_classification_title = second_data["title"]
                            if "children" in second_data and second_data["children"]:
                                for third_data in second_data["children"]:
                                    if third_data["title"] is None or "title" not in third_data.keys():
                                        secondary_classification_title = " "
                                    else:
                                        secondary_classification_title = third_data["title"]
                                    if "children" in third_data and third_data["children"]:
                                        for fourth_data in third_data["children"]:
                                            if "title" not in fourth_data.keys():
                                                fourth_data["title"] = " "
                                            elif fourth_data["title"] is None:
                                                fourth_data["title"] = " "
                                            tertiary_classification_title = fourth_data["title"]
                                            if "children" in fourth_data and fourth_data["children"]:
                                                for fifth_data in fourth_data["children"]:
                                                    if "title" not in fifth_data.keys():
                                                        fifth_data["title"] = " "
                                                    elif fifth_data["title"] is None:
                                                        fifth_data["title"] = " "
                                                    fourth_classification_title = fifth_data["title"]
                                                    if "children" in fifth_data and fifth_data["children"]:
                                                        for sixth_data in fifth_data["children"]:
                                                            if "title" not in sixth_data.keys():
                                                                sixth_data["title"] = " "
                                                            elif sixth_data["title"] is None:
                                                                sixth_data["title"] = " "
                                                            fifth_classification_title = sixth_data["title"]
                                                            if "children" in sixth_data and sixth_data["children"]:
                                                                for seventh_data in sixth_data["children"]:
                                                                    if seventh_data["title"] is None:
                                                                        seventh_data["title"] = " "
                                                                    seventh_classification_title = seventh_data["title"]
                                                                    title = disease_title + " -- " + primary_classification_title + " -- " + secondary_classification_title + " -- " + tertiary_classification_title + " -- " + fourth_classification_title + " -- " + fifth_classification_title + " -- " + seventh_classification_title
                                                                    test_indicator_list.append(title)
                                                            else:
                                                                title = disease_title + " -- " + primary_classification_title + " -- " + secondary_classification_title + " -- " + tertiary_classification_title + " -- " + fourth_classification_title + " -- " + fifth_classification_title
                                                                test_indicator_list.append(title)
                                                    else:
                                                        title = disease_title + " -- " + primary_classification_title + " -- " + secondary_classification_title + " -- " + tertiary_classification_title + " -- " + fourth_classification_title
                                                        test_indicator_list.append(title)
                                            else:
                                                title = disease_title + " -- " + primary_classification_title + " -- " + secondary_classification_title + " -- " + tertiary_classification_title
                                                test_indicator_list.append(title)
                                    else:
                                        title = disease_title + " -- " + primary_classification_title + " -- " + secondary_classification_title
                                        test_indicator_list.append(title)
            Assertions().assert_in_titan_data(standard_indicator_list, test_indicator_list, indicator_name)
    # return test_indicator_list, standard_indicator_list







# title_list = list()
#
# def get_data(first_data, data_list, title3):
#     if first_data["title"] is None or "title" not in first_data.keys():
#         title1 = ""
#     else:
#         title1 = first_data["title"]
#     if "children" in first_data and first_data["children"]:
#         for second_data in first_data["children"]:
#             # if second_data["title"] is None or "title" not in second_data.keys():
#             #     title2 = ""
#             # else:
#             #     title2 = second_data["title"]
#             title3 = title3 + "--" + title1
#             return get_data(second_data, data_list, title3)
#     else:
#         data_list.append(title3)
#         # b = "--".join(data_list)
#         # data_list.append(b)
#         return data_list

# def test(data):
#     test_list = list()
#     title = ""
#     for i in data:
#         p = i
#         # while "child" in p.keys():
#         while "children" in p and p["children"]:
#             title = p["title"] + "--" + title
#             p = p["children"]
#         test_list.append(title)
#     return test_list

# def get_indicator_data(response_data):
#     conf_indicator_list = ConfigYaml().get_titan_info()
#     for indicator_name in conf_indicator_list:
#         test_indicator_list = list()
#         file = Conf.get_titan_indicator_path() + os.sep + indicator_name + ".txt"
#         with open(file, "r", encoding="utf-8") as f:
#             standard_indicator_list = eval(f.read())
#             for first_data in response_data:
#                 disease_title = first_data["title"]
#                 if disease_title == indicator_name:
#                     test_indicator_list = test(first_data)
#                     print(test_indicator_list)
#             Assertions().assert_in_titan_data(standard_indicator_list, test_indicator_list, indicator_name)


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

