import json
import os
import allure
import pytest
from common.handle_test import Handle
from config import Conf
from utils.YamlUtil import YamlReader

get_patient_list = os.path.join(Conf.get_data_path(), "AKSO_getPatientList.yml")
patient_list = YamlReader(get_patient_list).read_data_all()

get_patients_with_cough = os.path.join(Conf.get_data_path(), "AKSO_patients_with_cough.yml")
patients_with_cough = YamlReader(get_patients_with_cough).read_list_data()

get_search_list = os.path.join(Conf.get_data_path(), "AKSO_getSearchInfo.yml")
search_info = YamlReader(get_search_list).read_list_data()

get_word_association = os.path.join(Conf.get_data_path(), "AKSO_getWordAssociation.yml")
word_association = YamlReader(get_word_association).read_list_data()

show_weight_template = os.path.join(Conf.get_data_path(), "AKSO_showWeightTemplate.yml")
weight_template = YamlReader(show_weight_template).read_list_data()

matchWeight = os.path.join(Conf.get_data_path(), "AKSO_matchWeight.yml")
match_weight = YamlReader(matchWeight).read_list_data()

getReportData = os.path.join(Conf.get_data_path(), "AKSO_getReportDatas.yml")
report_data = YamlReader(getReportData).read_data_all()

treatmentPathway = os.path.join(Conf.get_data_path(), "AKSO_treatmentPathway.yml")
treatment_pathway = YamlReader(treatmentPathway).read_list_data()

getTimeAxis = os.path.join(Conf.get_data_path(), "AKSO_getTimeAxis.yml")
get_time_axis = YamlReader(getTimeAxis).read_list_data()

patientContrast = os.path.join(Conf.get_data_path(), "AKSO_patientContrast.yml")
patient_contrast = YamlReader(patientContrast).read_list_data()

getRecord = os.path.join(Conf.get_data_path(), "AKSO_getRecord.yml")
get_record = YamlReader(getRecord).read_list_data()


@allure.feature("相似病例智能分析")
class TestAKSO:
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("p_info", patient_list)
    def test_get_patient_list(self, p_info):
        Handle().handle_test(p_info)

    @pytest.mark.dependency(name="cough")
    @pytest.mark.parametrize("p_cough", patients_with_cough)
    def test_get_patients_with_cough(self, p_cough):
        p_cough["data"]["paramJson"] = str(p_cough["data"]["paramJson"])
        body = Handle().handle_res_body(p_cough)
        global inpatientNo
        inpatientNo = body["responseData"]["content"][0]["INPATIENT_NO"]
        # file = Conf._config_login
        # with open(file, "r", encoding="utf-8") as f:
        #     login = yaml.safe_load(f)
        # login["login"]["inpatientNo"] = inpatientNo
        # with open(file, "w", encoding="utf-8") as f:
        #     yaml.dump(login, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)

    @pytest.mark.parametrize("s_info", search_info)
    def test_get_search_info(self, s_info):
        Handle().handle_test(s_info)

    @pytest.mark.parametrize("w_association", word_association)
    def test_get_word_association(self, w_association):
        Handle().handle_test(w_association)

    @pytest.mark.dependency(name="weight", depends=["cough"])
    @pytest.mark.parametrize("m_weight", match_weight)
    def test_match_weight(self, m_weight):
        m_weight["data"]["inpatientNo"] = inpatientNo
        Handle().handle_test(m_weight)
        body = Handle().handle_res_body(m_weight)
        global inpatient, score_str
        inpatient = ""
        score = {}
        local_data = body["resultData"]["localData"]
        for local in local_data:
            st = local["inpatient_no"] + "|" + local["hospital_code"] + ","
            inpatient = inpatient + st
        score_list = local_data[:2]
        for score_data in score_list:
            sc = {score_data["inpatient_no"] + "|" + score_data["hospital_code"]: score_data["similar_count"]}
            score.update(sc)
        score_str = str(json.dumps(score))

    @pytest.mark.dependency(depends=["weight"])
    @pytest.mark.parametrize("r_data", report_data)
    def test_report_data(self, r_data):
        r_data["data"]["inPatientNos"] = inpatient
        Handle().handle_test(r_data)

    @pytest.mark.dependency(depends=["weight"])
    @pytest.mark.parametrize("t_pathway", treatment_pathway)
    def test_treatment_pathway(self, t_pathway):
        t_pathway["data"]["inPatientNos"] = inpatient
        Handle().handle_test(t_pathway)

    @pytest.mark.dependency(depends=["weight"])
    @pytest.mark.parametrize("time_axis", get_time_axis)
    def test_get_time_axis(self, time_axis):
        time_axis["data"]["inPatientNo"] = inpatientNo
        Handle().handle_test(time_axis)

    @pytest.mark.dependency(depends=["weight", "cough"])
    @pytest.mark.parametrize("p_contrast", patient_contrast)
    def test_patient_contrast(self, p_contrast):
        p_contrast["data"]["inPatientNo"] = inpatientNo
        p_contrast["data"]["scoreData"] = score_str
        Handle().handle_test(p_contrast)

    @pytest.mark.dependency(depends=["weight"])
    @pytest.mark.parametrize("g_record", get_record)
    def test_get_record(self, g_record):
        g_record["expect"] = inpatientNo
        Handle().handle_test(g_record)
