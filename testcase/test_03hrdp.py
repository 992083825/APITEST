# import os
# import random
#
# import allure
# import pytest
# from config import Conf
# from common.handle_test import Handle
# from utils.YamlUtil import YamlReader
#
# newDisease = os.path.join(Conf.get_data_path(), "HRDP_newDisease.yml")
# new_disease = YamlReader(newDisease).read_list_data()
#
# diseasesList = os.path.join(Conf.get_data_path(), "HRDP_diseasesList.yml")
# diseases_list = YamlReader(diseasesList).read_list_data()
#
# newDepartment = os.path.join(Conf.get_data_path(), "HRDP_newDepartment.yml")
# new_department = YamlReader(newDepartment).read_list_data()
#
# departmentList = os.path.join(Conf.get_data_path(), "HRDP_departmentList.yml")
# department_list = YamlReader(departmentList).read_list_data()
#
# newSubDepartment = os.path.join(Conf.get_data_path(), "HRDP_newSubDepartment.yml")
# new_sub_department = YamlReader(newSubDepartment).read_list_data()
#
# editDepartment = os.path.join(Conf.get_data_path(), "HRDP_editDepartment.yml")
# edit_department = YamlReader(editDepartment).read_list_data()
#
# choiceEvaluate = os.path.join(Conf.get_data_path(), "HRDP_choiceEvaluate.yml")
# choice_evaluate = YamlReader(choiceEvaluate).read_list_data()
#
# newEvaluate = os.path.join(Conf.get_data_path(), "HRDP_newEvaluate.yml")
# new_evaluate = YamlReader(newEvaluate).read_list_data()
#
# evaluateList = os.path.join(Conf.get_data_path(), "HRDP_evaluateList.yml")
# evaluate_list = YamlReader(evaluateList).read_list_data()
#
# updateEvaluate = os.path.join(Conf.get_data_path(), "HRDP_updateEvaluate.yml")
# update_evaluate = YamlReader(updateEvaluate).read_list_data()
#
# disableEvaluate = os.path.join(Conf.get_data_path(), "HRDP_disableEvaluate.yml")
# disable_evaluate = YamlReader(disableEvaluate).read_data_all()
#
# patientSearch = os.path.join(Conf.get_data_path(), "HRDP_patientSearch.yml")
# patient_search = YamlReader(patientSearch).read_list_data()
#
# createAnswer = os.path.join(Conf.get_data_path(), "HRDP_createAnswer.yml")
# create_answer = YamlReader(createAnswer).read_list_data()
#
# evaluateSupport = os.path.join(Conf.get_data_path(), "HRDP_evaluateSupport.yml")
# evaluate_support = YamlReader(evaluateSupport).read_list_data()
#
# evaluateInfo = os.path.join(Conf.get_data_path(), "HRDP_evaluateInfo.yml")
# evaluate_info = YamlReader(evaluateInfo).read_list_data()
#
# getQtContent = os.path.join(Conf.get_data_path(), "HRDP_getQtContent.yml")
# get_qt_content = YamlReader(getQtContent).read_list_data()
#
# detailEvaluate = os.path.join(Conf.get_data_path(), "HRDP_detailEvaluate.yml")
# detail_evaluate = YamlReader(detailEvaluate).read_list_data()
#
# submitEvaluate = os.path.join(Conf.get_data_path(), "HRDP_submitEvaluate.yml")
# submit_evaluate = YamlReader(submitEvaluate).read_list_data()
#
# evaluateData = os.path.join(Conf.get_data_path(), "HRDP_evaluateData.yml")
# evaluate_data = YamlReader(evaluateData).read_list_data()
#
# evaluateAnswerList = os.path.join(Conf.get_data_path(), "HRDP_evaluateAnswerList.yml")
# evaluate_answer_list = YamlReader(evaluateAnswerList).read_list_data()
#
# queryCommitAnswer = os.path.join(Conf.get_data_path(), "HRDP_queryCommitAnswer.yml")
# query_commit_answer = YamlReader(queryCommitAnswer).read_list_data()
#
# getEvaluateScore = os.path.join(Conf.get_data_path(), "HRDP_getEvaluateScore.yml")
# get_evaluate_score = YamlReader(getEvaluateScore).read_list_data()
#
# evaluateAnalysis = os.path.join(Conf.get_data_path(), "HRDP_evaluateAnalysis.yml")
# evaluate_analysis = YamlReader(evaluateAnalysis).read_list_data()
#
# evaluateDelete = os.path.join(Conf.get_data_path(), "HRDP_evaluateDelete.yml")
# evaluate_delete = YamlReader(evaluateDelete).read_list_data()
#
# departmentDelete = os.path.join(Conf.get_data_path(), "HRDP_departmentDelete.yml")
# department_delete = YamlReader(departmentDelete).read_list_data()
#
# diseasesDelete = os.path.join(Conf.get_data_path(), "HRDP_diseasesDelete.yml")
# diseases_delete = YamlReader(diseasesDelete).read_list_data()
#
#
# @allure.feature("高危疾病风险预测")
# class TestHRDP:
#
#     @pytest.mark.parametrize("n_disease", new_disease)
#     def test_new_disease(self, n_disease):
#         Handle().handle_test(n_disease)
#
#     @pytest.mark.dependency(name="diseases_list")
#     @pytest.mark.parametrize("dis_list", diseases_list)
#     def test_diseases_list(self, dis_list):
#         body = Handle().handle_res_body(dis_list)
#         global diseasesId
#         diseasesId = body["data"]["content"][0]["id"]
#         Handle().handle_test(dis_list)
#
#     @pytest.mark.parametrize("n_department", new_department)
#     def test_new_department(self, n_department):
#         Handle().handle_test(n_department)
#
#     @pytest.mark.dependency(name="parent_department")
#     @pytest.mark.parametrize("dep_list", department_list)
#     def test_department_list(self, dep_list):
#         body = Handle().handle_res_body(dep_list)
#         global departmentId
#         departmentId = body["data"][0]["id"]
#         Handle().handle_test(dep_list)
#
#     @pytest.mark.dependency(depends=["diseases_list", "parent_department"])
#     @pytest.mark.parametrize("sub_department", new_sub_department)
#     def test_new_sub_department(self, sub_department):
#         sub_department["data"]["diseases"] = diseasesId
#         sub_department["data"]["parentId"] = departmentId
#         Handle().handle_test(sub_department)
#
#     @pytest.mark.dependency(depends=["parent_department"])
#     @pytest.mark.parametrize("e_department", edit_department)
#     def test_edit_department(self, e_department):
#         e_department["data"]["departmentId"] = departmentId
#         Handle().handle_test(e_department)
#
#     @pytest.mark.dependency(name="choice_evaluate")
#     @pytest.mark.parametrize("c_evaluate", choice_evaluate)
#     def test_choice_evaluate(self, c_evaluate):
#         body = Handle().handle_res_body(c_evaluate)
#         global qtUrl, evaluate_title
#         qtUrl = body["data"][0]["URL"]
#         evaluate_title = body["data"][0]["TITLE"]
#         Handle().handle_test(c_evaluate)
#
#     @pytest.mark.dependency(depends=["diseases_list", "choice_evaluate"])
#     @pytest.mark.parametrize("n_evaluate", new_evaluate)
#     def test_new_evaluate(self, n_evaluate):
#         n_evaluate["data"]["qtUrl"] = qtUrl
#         n_evaluate["data"]["diseasesList"][0] = diseasesId
#         Handle().handle_test(n_evaluate, data_type="json")
#
#     @pytest.mark.dependency(name="evaluate_list", depends=["choice_evaluate"])
#     @pytest.mark.parametrize("eva_list", evaluate_list)
#     def test_evaluate_list(self, eva_list):
#         global qtId, evaluate_id
#         eva_list["data"]["qtTitle"] = evaluate_title
#         eva_list["expect"] = evaluate_title
#         body = Handle().handle_res_body(eva_list)
#         evaluate_id = body["data"]["content"][0]["id"]
#         qtId = body["data"]["content"][0]["qtId"]
#         Handle().handle_test(eva_list)
#         print(evaluate_id)
#
#     @pytest.mark.dependency(depends=["diseases_list", "choice_evaluate"])
#     @pytest.mark.parametrize("up_evaluate", update_evaluate)
#     def test_update_evaluate(self, up_evaluate):
#         up_evaluate["data"]["qtUrl"] = qtUrl
#         up_evaluate["data"]["diseasesList"][0] = diseasesId
#         Handle().handle_test(up_evaluate, data_type="json")
#
#     @pytest.mark.dependency(depends=["diseases_list"])
#     @pytest.mark.parametrize("dis_evaluate", disable_evaluate)
#     def test_disable_evaluate(self, dis_evaluate):
#         dis_evaluate["data"]["id"] = evaluate_id
#         Handle().handle_test(dis_evaluate)
#
#     @pytest.mark.dependency(name="patient_search", depends=["choice_evaluate"])
#     @pytest.mark.parametrize("pat_search", patient_search)
#     def test_patient_search(self, pat_search):
#         global patiId
#         body = Handle().handle_res_body(pat_search)
#         patiId = body["responseData"]["content"][0]["patiId"]
#         Handle().handle_test(pat_search)
#
#     @pytest.mark.dependency(name="create_answer", depends=["choice_evaluate"])
#     @pytest.mark.parametrize("cre_answer", create_answer)
#     def test_create_answer(self, cre_answer):
#         global answerId
#         cre_answer["data"]["url"] = qtUrl
#         cre_answer["expect"] = evaluate_title
#         body = Handle().handle_res_body(cre_answer)
#         answerId = body["data"][str(qtUrl)]["answerId"]
#         Handle().handle_test(cre_answer)
#         print(answerId)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("eva_support", evaluate_support)
#     def test_eva_support(self, eva_support):
#         eva_support["data"]["qtUrl"] = qtUrl
#         eva_support["expect"] = qtUrl
#         Handle().handle_test(eva_support)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("eva_info", evaluate_info)
#     def test_evaluate_info(self, eva_info):
#         eva_info["data"]["qtUrl"] = qtUrl
#         eva_info["expect"][0] = qtUrl
#         Handle().handle_test(eva_info)
#
#     @pytest.mark.dependency(name="qt_content", depends=["choice_evaluate"])
#     @pytest.mark.parametrize("qt_content", get_qt_content)
#     def test_get_qt_content(self, qt_content):
#         global context
#         context = list()
#         qt_content["data"]["url"] = qtUrl
#         body = Handle().handle_res_body(qt_content)
#         items = body["data"][0]["item"]
#         for item in items:
#             linkId = item["linkId"]
#             sectionItemRId = item["sectionItemRId"]
#             showType = item["showType"]
#             if "option" in item:
#                 code = random.randint(0, len(item["option"]) - 1)
#                 display = item["option"][code]["value"]["display"]
#                 sectionItemOptionRId = item["option"][code]["value"]["itemOptionRId"]
#                 text = {
#                     "linkId": linkId, "sectionItemRId": sectionItemRId, "showType": showType,
#                     "value": [{
#                         "display": display, "code": code, "content": "",
#                         "sectionItemOptionRId": sectionItemOptionRId
#                     }]
#                 }
#                 context.append(text)
#         Handle().handle_test(qt_content)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("det_evaluate", detail_evaluate)
#     def test_detail_evaluate(self, det_evaluate):
#         det_evaluate["data"]["qtUrl"] = qtUrl
#         Handle().handle_test(det_evaluate)
#
#     @pytest.mark.dependency(
#         depends=["choice_evaluate", "patient_search", "create_answer", "evaluate_list", "qt_content"])
#     @pytest.mark.parametrize("sub_evaluate", submit_evaluate)
#     def test_submit_evaluate(self, sub_evaluate):
#         sub_evaluate["data"]["reqJson"]["patiId"] = patiId
#         sub_evaluate["data"]["reqJson"] = str(sub_evaluate["data"]["reqJson"])
#         sub_evaluate["data"]["answerId"] = answerId
#         sub_evaluate["data"]["qtId"] = qtId
#         sub_evaluate["data"]["context"] = str(context)
#         Handle().handle_test(sub_evaluate)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("eva_data", evaluate_data)
#     def test_evaluate_data(self, eva_data):
#         eva_data["data"]["qtUrl"] = qtUrl
#         Handle().handle_test(eva_data)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("answer_list", evaluate_answer_list)
#     def test_evaluate_answer_list(self, answer_list):
#         answer_list["data"]["qtUrl"] = qtUrl
#         Handle().handle_test(answer_list)
#
#     @pytest.mark.dependency(depends=["create_answer"])
#     @pytest.mark.parametrize("commit_answer", query_commit_answer)
#     def test_query_commit_answer(self, commit_answer):
#         commit_answer["data"]["answerId"] = answerId
#         Handle().handle_test(commit_answer)
#
#     @pytest.mark.dependency(depends=["patient_search"])
#     @pytest.mark.parametrize("evaluate_score", get_evaluate_score)
#     def test_get_evaluate_score(self, evaluate_score):
#         evaluate_score["data"]["answerPatientId"] = answerId
#         Handle().handle_test(evaluate_score)
#
#     @pytest.mark.dependency(depends=["choice_evaluate", "patient_search"])
#     @pytest.mark.parametrize("eva_analysis", evaluate_analysis)
#     def test_get_evaluate_analysis(self, eva_analysis):
#         eva_analysis["data"]["answerPatientId"] = patiId
#         eva_analysis["data"]["qtUrl"] = qtUrl
#         Handle().handle_test(eva_analysis)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("eva_delete", evaluate_delete)
#     def test_evaluate_delete(self, eva_delete):
#         eva_delete["data"]["qtUrl"] = qtUrl
#         Handle().handle_test(eva_delete)
#
#     @pytest.mark.dependency(depends=["choice_evaluate"])
#     @pytest.mark.parametrize("dep_delete", department_delete)
#     def test_department_delete(self, dep_delete):
#         dep_delete["data"]["departmentId"] = departmentId
#         Handle().handle_test(dep_delete)
#
#     @pytest.mark.dependency(depends=["diseases_list"])
#     @pytest.mark.parametrize("dis_delete", diseases_delete)
#     def test_diseases_delete(self, dis_delete):
#         dis_delete["data"]["id"] = diseasesId
#         Handle().handle_test(dis_delete)
