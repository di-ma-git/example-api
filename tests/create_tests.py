import urls
from data import MultipartFormData
from data import Data
from data import Data_doc
import requests
import pytest
import helper
from api.create import Create


class TestCreate:
    source_value = ['CRM_VOLGA_V2', 'CRM_SOUTH_V2', 'CRM_URAL_V2', 'CRM_NORTH_WEST_V2', 'CRM_FAR_EAST_V2',
                    'CRM_SIBERIA_V2']
    type_task = ['CONTRACT', 'CONTRACT_ALADDIN', 'PAID_WORK_ACT', 'CONTRACT_MEGAFON']
    type_doc = ['TEMPORARY_CERTIFICATE', 'OFFICER_CERTIFICATE', 'MILITARY_TICKET',
                'REFUGEE_CERTIFICATE', 'REFUGEE_IMMIGRANTS_CERTIFICATE', 'CERTIFICATE_OF_ASYLUM']

    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_task', type_task)
    def test_create_for_all_process(self, source_value, type_task):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_contract, source_value, type_task)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    source_value_for_ural = ['CRM_URAL_V2']
    type_for_ural = ['TERMINATION', 'RENEWAL']

    @pytest.mark.parametrize('source_value_for_ural', source_value_for_ural)
    @pytest.mark.parametrize('type_for_ural', type_for_ural)
    def test_create_for_ural(self, source_value_for_ural, type_for_ural):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_contract, source_value_for_ural, type_for_ural)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    source_value_for_north_west = ['CRM_NORTH_WEST_V2']
    type_for_north_west = ['CONVERGENT']

    @pytest.mark.parametrize('source_value_for_north_west', source_value_for_north_west)
    @pytest.mark.parametrize('type_for_north_west', type_for_north_west)
    def test_create_for_norw_west(self, source_value_for_north_west, type_for_north_west):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_contract, source_value_for_north_west,
                                                               type_for_north_west)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    type_act = ['TRANSFER_ACT']

    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_act', type_act)
    def test_create_for_act(self, source_value, type_act):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_act_transfer, source_value, type_act)
        response = Create.create_and_cancel(data)
        print(response.text)
        assert response.status_code == 201 and response.json() is not None

    type_crm = ['MNP_CRM']

    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_crm', type_crm)
    def test_create_for_crm(self, source_value, type_crm):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_contract_crm, source_value, type_crm)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    type_dzo = ['CONTRACT_DZO']
    source_dzo = ['CRM_NORTH_WEST_V2', 'CRM_FAR_EAST_V2']

    @pytest.mark.parametrize('type_dzo', type_dzo)
    @pytest.mark.parametrize('source_dzo', source_dzo)
    def test_create_for_dzo(self, source_dzo, type_dzo):
        data = helper.ChangeTestDataHelper.modify_payload_body_type_dzo(Data.data_contract, source_dzo, type_dzo)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    @pytest.mark.parametrize('type_proc, source', Data_doc.DATA_ATTORNEY)
    def test_create_for_attor_doc(self, type_proc, source):
        data = helper.ChangeTestDataHelper.modify_payload_body(Data.data_contract_attorney, source, type_proc)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    @pytest.mark.parametrize('type_proc, source', Data_doc.DATA_TEMPORARY_CERTIFICATE_AND_CO)
    @pytest.mark.parametrize('type_doc', type_doc)
    def test_create_for_doc_temp(self, type_proc, source, type_doc):
        data = helper.ChangeTestDataHelper.modify_payload_body_doc(Data.data_contract, source, type_proc, type_doc)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    type_term = ['TEMPMILITARYID']
    @pytest.mark.parametrize('type_proc, source', Data_doc.DATA_TEMPMILITARYID)
    @pytest.mark.parametrize('type_term', type_term)
    def test_create_for_doc_pass_sal(self, type_proc, source, type_term):
        data = helper.ChangeTestDataHelper.modify_payload_body_doc(Data.data_contract, source, type_proc, type_term)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None

    type_pass_foreigner = ['RESIDENCY','TEMPORARY_RESIDENCE','MIGRATION_CARD']

    @pytest.mark.parametrize('type_proc, source', Data_doc.DATA_PASSPORT_FOREIGNER)
    @pytest.mark.parametrize('type_pass_foreigner', type_pass_foreigner)
    def test_create_for_doc_pass_foreigner(self, type_proc, source, type_pass_foreigner):
        data = helper.ChangeTestDataHelper.modify_payload_body_doc(Data.data_password_foreigner, source, type_proc, type_pass_foreigner)
        response = Create.create_and_cancel(data)
        assert response.status_code == 201 and response.json() is not None
