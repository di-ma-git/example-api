import requests
import json
import warnings
import pytest
from data import MultipartFormData
from data import Data
import time
import urls

env_url = "https://devapi.ed.rt.ru"
type_task = "CONTRACT"
source = "CRM_VOLGA_V2"
branch = "80"
account = "300300400500"
nationality = "RUS"
phone = "9333333331"
warnings.filterwarnings("ignore")


class Search:
    @staticmethod
    def search_v1(phone):
        mh = MultipartFormData.format(data=Data.data_contract, headers=Data.headers)
        url = urls.BASE_URL_DEV + urls.SEARCH_V1 + phone
        response = requests.request("POST", url, headers=Data.headers1, verify=False)
        temp = response.json()['searchResults']
        taskId_search = temp[0]['taskId']
        url = urls.BASE_URL_DEV +urls.CREATE_TASK + taskId_search + "/cancel?reason=OK"
        requests.request("POST", url, headers=Data.headers1, verify=False)
        print(response.text)
        return response

    @staticmethod
    def search_v2(account):
        mh = MultipartFormData.format(data=Data.data_contract, headers=Data.headers)
        url = urls.BASE_URL_DEV + urls.SEARCH_V2 + account
        response = requests.request("POST", url, headers=Data.headers1, verify=False)
        temp = response.json()['searchResults']
        taskId_search = temp[0]['taskId']
        url = urls.BASE_URL_DEV + urls.CREATE_TASK + taskId_search + "/cancel?reason=OK"
        requests.request("POST", url, headers=Data.headers1, verify=False)
        print(response.text)
        return response

    @staticmethod
    def search_v3(account, order):
        mh = MultipartFormData.format(data=Data.data_contract, headers=Data.headers)
        url = urls.BASE_URL_DEV + urls.SEARCH_V3_ONE_PART + account + urls.SEARCH_V3_TWO_PART + order
        response = requests.request("POST", url, headers=Data.headers1, verify=False)
        temp = response.json()['searchResults']
        taskId_search = temp[0]['taskId']
        url = urls.BASE_URL_DEV + urls.CREATE_TASK + taskId_search + "/cancel?reason=OK"
        requests.request("POST", url, headers=Data.headers1, verify=False)
        print(response.text)
        return response
