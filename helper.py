import requests
from data import MultipartFormData
from data import Data
import random
import urls


class Metods:
    @staticmethod
    def download(taskId):
        mh = MultipartFormData.format(data=Data.data_download, headers=Data.headers1)
        url = urls.BASE_URL_DEV + urls.CREATE_TASK + taskId + urls.UPLOAD
        print(url)
        response = requests.request("POST", url, headers=Data.headers, data=mh, verify=False)
        print(response.text)


class ChangeTestDataHelper:
    @staticmethod
    def modify_payload_body(body, source_value, type_task):
        body_new = body.copy()
        body_new["data"]["key"] = str(random.randint(1000, 1000000))
        body_new["data"]["source"] = source_value
        body_new["data"]["type"] = type_task

        return body_new

    @staticmethod
    def modify_payload_body_type_dzo(body, source_value, type_task):
        body_new = body.copy()
        body_new["data"]["key"] = str(random.randint(1000, 1000000))
        body_new["data"]["source"] = source_value
        body_new["data"]["type"] = type_task
        if body_new["data"]["source"] == 'CRM_NORTH_WEST_V2':
            body_new["data"]["provider"] = 'ATK'
        else:
            body_new["data"]["provider"] = 'ALIANCE'
        return body_new

    @staticmethod
    def modify_payload_body_doc(body, source_value, type_task, type_doc_rus):
        body_new = body.copy()
        body_new["data"]["key"] = str(random.randint(1000, 1000000))
        body_new["data"]["source"] = source_value
        body_new["data"]["type"] = type_task
        body_new["data"]["content"]["documents"][0]["type"] = type_doc_rus

        return body_new

    @staticmethod
    def modify_payload_body_for_search(body, source_value, type_task):
        body_new = body.copy()
        body_new["data"]["key"] = str(random.randint(1000, 1000000))
        body_new["data"]["source"] = source_value
        body_new["data"]["type"] = type_task
        body_new["data"]["identificationValue"] = "9" + str(random.randint(100000000, 999999999))
        body_new["data"]["content"]["contract"]["account"] = "3" + str(random.randint(10000000000, 99999999999))

        return body_new




