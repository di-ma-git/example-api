from data import Data
from data import Data_doc
import requests
import pytest
import helper
from api.create import Create
from api.search import Search
from api.cancel import Cancel


class TestSearch:
    source_value = ['CRM_VOLGA_V2', 'CRM_SOUTH_V2']
    type_task = ['CONTRACT', 'CONTRACT_ALADDIN', 'PAID_WORK_ACT', 'CONTRACT_MEGAFON']

    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_task', type_task)
    def test_create_one_task_and_search_v1(self, source_value, type_task):
        data = helper.ChangeTestDataHelper.modify_payload_body_for_search(Data.data_contract, source_value, type_task)
        response_create = Create.create_for_search(data)
        taskId_create = response_create.json()['taskId']
        phone = data["data"]["identificationValue"]
        response_search = Search.search_v1(phone)
        temp = response_search.json()['searchResults']
        taskId_search = temp[0]['taskId']
        print(response_search)
        assert response_search.status_code == 200 and taskId_create == taskId_search


    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_task', type_task)
    def test_create_one_task_and_search_v2(self, source_value, type_task):
        data = helper.ChangeTestDataHelper.modify_payload_body_for_search(Data.data_contract, source_value, type_task)
        response_create = Create.create_for_search(data)
        taskId_create = response_create.json()['taskId']
        account = data["data"]["content"]["contract"]["account"]
        response_search = Search.search_v2(account)
        temp = response_search.json()['searchResults']
        taskId_search = temp[0]['taskId']
        print(response_search)
        assert response_search.status_code == 200 and taskId_create == taskId_search

    @pytest.mark.parametrize('source_value', source_value)
    @pytest.mark.parametrize('type_task', type_task)
    def test_create_one_task_and_search_v3(self, source_value, type_task):
        data = helper.ChangeTestDataHelper.modify_payload_body_for_search(Data.data_contract, source_value, type_task)
        response_create = Create.create_for_search(data)
        taskId_create = response_create.json()['taskId']
        account = data["data"]["content"]["contract"]["account"]
        order = data["data"]["content"]["wfm"]["order"]
        response_search = Search.search_v3(account, order)
        temp = response_search.json()['searchResults']
        taskId_search = temp[0]['taskId']
        print(response_search)
        assert response_search.status_code == 200 and taskId_create == taskId_search



