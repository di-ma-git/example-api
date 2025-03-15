import urls
from data import MultipartFormData
from data import Data
import requests
import pytest
import helper


class Create:
    @staticmethod
    def create_and_cancel(data):
        mh = MultipartFormData.format(data=data, headers=Data.headers)
        url = urls.BASE_URL_DEV + urls.CREATE_TASK
        response = requests.request("POST", url, headers=Data.headers, data=mh, verify=False)
        print(response.text)
        if not response.json()["success"]:
            temp = response.json()["error"]
            url1 = url + temp['taskId'] + "/cancel?reason=OK"
            print(url1)
            requests.request("POST", url1, headers=Data.headers1, verify=False)
            mh = MultipartFormData.format(data=Data.data, headers=Data.headers)
            url = urls.BASE_URL_DEV + urls.CREATE_TASK
            response = requests.request("POST", url, headers=Data.headers, data=mh, verify=False)
            print(response.text)
        url1 = url + response.json()["taskId"] + "/cancel?reason=OK"
        print(url1)
        requests.request("POST", url1, headers=Data.headers1, verify=False)
        return response

    @staticmethod
    def create_for_search(data):
        mh = MultipartFormData.format(data=data, headers=Data.headers)
        url = urls.BASE_URL_DEV + urls.CREATE_TASK
        response = requests.request("POST", url, headers=Data.headers, data=mh, verify=False)
        print(response.text)
        return response
