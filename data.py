branch = "80"
account = "300300400500"
nationality = "RUS"
phone = "9333333331"

class Data_doc:
    DATA_ATTORNEY = [['CONTRACT', 'CRM_VOLGA_V2'], ['PAID_WORK_ACT', 'CRM_VOLGA_V2'], ['CONTRACT', 'CRM_SOUTH_V2'],
            ['PAID_WORK_ACT', 'CRM_SOUTH_V2'], ['PAID_WORK_ACT', 'CRM_URAL_V2'],
            ['CONTRACT', 'CRM_NORTH_WEST_V2'], ['CONVERGENT', 'CRM_NORTH_WEST_V2'],
            ['CONTRACT_DZO', 'CRM_NORTH_WEST_V2'], ['PAID_WORK_ACT', 'CRM_NORTH_WEST_V2'],
            ['PAID_WORK_ACT', 'CRM_FAR_EAST_V2'], ['PAID_WORK_ACT', 'CRM_SIBERIA_V2']]

    DATA_TEMPORARY_CERTIFICATE_AND_CO =[['PAID_WORK_ACT', 'CRM_VOLGA_V2'], ['CONTRACT', 'CRM_SOUTH_V2'], ['PAID_WORK_ACT', 'CRM_SOUTH_V2'],
            ['PAID_WORK_ACT', 'CRM_URAL_V2'], ['CONTRACT', 'CRM_NORTH_WEST_V2'],
            ['CONVERGENT', 'CRM_NORTH_WEST_V2'], ['CONTRACT_DZO', 'CRM_NORTH_WEST_V2'],
            ['PAID_WORK_ACT', 'CRM_NORTH_WEST_V2'], ['CONTRACT', 'CRM_FAR_EAST_V2'],
            ['PAID_WORK_ACT', 'CRM_FAR_EAST_V2'], ['PAID_WORK_ACT', 'CRM_SIBERIA_V2']]

    DATA_TEMPMILITARYID = [['PAID_WORK_ACT', 'CRM_VOLGA_V2'], ['CONTRACT', 'CRM_SOUTH_V2'],
                                         ['PAID_WORK_ACT', 'CRM_SOUTH_V2'],
                                         ['PAID_WORK_ACT', 'CRM_URAL_V2'],
                                         ['PAID_WORK_ACT', 'CRM_NORTH_WEST_V2'], ['CONTRACT', 'CRM_FAR_EAST_V2'],
                                         ['PAID_WORK_ACT', 'CRM_FAR_EAST_V2'], ['PAID_WORK_ACT', 'CRM_SIBERIA_V2']]

    DATA_PASSPORT_FOREIGNER = [['PAID_WORK_ACT', 'CRM_VOLGA_V2'], ['CONTRACT', 'CRM_SOUTH_V2'],
                           ['PAID_WORK_ACT', 'CRM_SOUTH_V2'],
                           ['PAID_WORK_ACT', 'CRM_URAL_V2'],
                           ['PAID_WORK_ACT', 'CRM_NORTH_WEST_V2'],
                           ['PAID_WORK_ACT', 'CRM_FAR_EAST_V2'], ['PAID_WORK_ACT', 'CRM_SIBERIA_V2']]


class MultipartFormData(object):
    "" "преобразование формата multipart / form-data" ""

    @staticmethod
    def format(data, boundary="----WebKitFormBoundary7MA4YWxkTrZu0gW", headers={}):
        if "content-type" in headers:
            fd_val = str(headers["content-type"])
            if "boundary" in fd_val:
                fd_val = fd_val.split(";")[1].strip()
                boundary = fd_val.split("=")[1].strip()
            else:
                raise "Информация заголовка multipart / form-data неверна, проверьте, содержит ли ключ типа содержимого границу"

        json_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\nContent-Type: application/json\r\n\r\n{}\r\n'
        end_str = "--{}--".format(boundary)
        args_str = ""

        if not isinstance(data, dict):
            raise "Ошибка параметра multipart / form-data, параметр данных должен иметь тип dict"
        for key, value in data.items():
            args_str = args_str + json_str.format(boundary, key, value)

        args_str = args_str + end_str.format(boundary)
        args_str = args_str.replace("\'", "\"")
        return args_str


class Data:
    data_contract = {
        "data": {
            "type": "",
            "source": "",
            "provider": "",
            "product": "",
            "branch": branch,
            "key": "",
            "identificationParameter": "PHONE",
            "identificationValue": phone,
            "content": {
                "contract": {
                    "paymentMethod": "CREDIT",
                    "deliveryMethod": "EMAIL",
                    "consentToReceiveAdvertising": "true",
                    "consentToSmsInform": "true",
                    "consentToUseSubscriberData": "true",
                    "account": account,
                    "installerCode": "123456"
                },
                "client": {
                    "phone": "9993000299",
                    "sex": "FEMALE",
                    "email": "olga.y.belova@volga.rt.ru",
                    "nationality": nationality
                },
                "documents": [
                    {
                        "type": "PASSPORT_RU",
                        "affiliation": "CLIENT"
                    }],
                "registrationAddress": {
                    "globalId": 4046576
                },
                "installationAddress": {
                    "globalId": 4046576
                },
                "wfm": {
                    "order": "2148312248"
                }

            }
        }
    }
    data_act_transfer = {
        "data": {
            "type": "",
            "source": "",
            "branch": branch,
            "key": "",
            "identificationParameter": "PHONE",
            "identificationValue": phone,
            "content": {
                "contract": {
                    "paymentMethod": "CREDIT",
                    "deliveryMethod": "EMAIL",
                    "consentToReceiveAdvertising": "true",
                    "consentToSmsInform": "true",
                    "consentToUseSubscriberData": "true",
                    "account": account,
                    "installerCode": "123456",
                    "contractDate": "12.07.2024",
                    "contractNumber": "123412"

                },
                "client": {
                    "phone": "9993000299",
                    "sex": "FEMALE",
                    "email": "olga.y.belova@volga.rt.ru",
                    "nationality": ""
                },
                "registrationAddress": {
                    "globalId": 4046576
                },
                "installationAddress": {
                    "globalId": 4046576
                },
                "transfer": {
                    "totalCost": "",
                    "transferredEquipments": [
                        {
                            "equipmentName": "AQ",
                            "equipmentSerialNumber": "564",
                            "equipmentMacAddress": "f5.454.323.456.35",
                            "equipmentCondition": "new",
                            "equipmentPrice": "0",
                            "installment": {
                                "firstPayment": "0",
                                "installmentTerm": "3",
                                "installmentPlan": "new plan",
                                "regularPayment": "555.99",
                                "firstPaymentDate": "25.07.2024",
                                "lastPaymentDate": "28.07.2024"
                            }
                        }
                    ]
                }
            }
        }
    }
    data_contract_crm = {
        "data": {
            "type": "",
            "source": "",
            "branch": branch,
            "key": "",
            "identificationParameter": "PHONE",
            "identificationValue": phone,
            "content": {
                "contract": {
                    "paymentMethod": "CREDIT",
                    "deliveryMethod": "EMAIL",
                    "consentToReceiveAdvertising": "true",
                    "consentToSmsInform": "true",
                    "consentToUseSubscriberData": "true",
                    "installerCode": "123456"
                },
                "client": {
                    "phone": "9993000299",
                    "sex": "FEMALE",
                    "email": "olga.y.belova@volga.rt.ru",
                    "nationality": nationality
                },
                "documents": [
                    {
                        "type": "PASSPORT_RU",
                        "affiliation": "CLIENT"
                    }],
                "registrationAddress": {
                    "globalId": 4046576
                },
                "installationAddress": {
                    "globalId": 4046576
                },
                "wfm": {
                    "order": 2148312248
                }

            }
        }
    }

    data_contract_attorney = {
        "data": {
            "type": "",
            "source": "",
            "branch": branch,
            "key": "",
            "identificationParameter": "PHONE",
            "identificationValue": phone,
            "content": {
                "contract": {
                    "account": account,
                    "paymentMethod": "CREDIT",
                    "deliveryMethod": "EMAIL",
                    "consentToReceiveAdvertising": "true",
                    "consentToSmsInform": "true",
                    "consentToUseSubscriberData": "true",
                    "installerCode": "123456"
                },
                "client": {
                    "phone": "9993000299",
                    "sex": "FEMALE",
                    "email": "olga.y.belova@volga.rt.ru",
                    "nationality": nationality
                },
                "documents": [
                    {
                        "type": "ATTORNEY",
                        "affiliation": "CLIENT"
                    },
                    {
                        "type": "PASSPORT_RU",
                        "affiliation": "CLIENT"

                    },
                    {
                        "type": "PASSPORT_RU",
                        "affiliation": "REPRESENTATIVE"
                    }
                ],
                "registrationAddress": {
                    "globalId": 4046576
                },
                "installationAddress": {
                    "globalId": 4046576
                },
                "wfm": {
                    "order": 2148312248
                }

            }
        }
    }

    data_password_foreigner = {
        "data": {
            "type": "",
            "source": "",
            "branch": branch,
            "key": "",
            "identificationParameter": "PHONE",
            "identificationValue": phone,
            "content": {
                "contract": {
                    "account": account,
                    "paymentMethod": "CREDIT",
                    "deliveryMethod": "EMAIL",
                    "consentToReceiveAdvertising": "true",
                    "consentToSmsInform": "true",
                    "consentToUseSubscriberData": "true",
                    "installerCode": "123456"
                },
                "client": {
                    "phone": "9993000299",
                    "sex": "FEMALE",
                    "email": "olga.y.belova@volga.rt.ru",
                    "nationality": "BEL"
                },
                "documents": [
                    {
                        "type": "MIGRATION_CARD",
                        "affiliation": "CLIENT"

                    },
                    {
                        "type": "PASSPORT_FOREIGNER",
                        "affiliation": "CLIENT"


                    }
                ],
                "registrationAddress": {
                    "globalId": 4046576
                },
                "installationAddress": {
                    "globalId": 4046576
                },
                "wfm": {
                    "order": 2148312248
                }

            }
        }
    }

    headers = {
        'Authorization': 'Basic ZWRfcWFfdGVzdDpDZTFCJFRNc1ZFaU0=',
        'User-Agent': 'PostmanRuntime/7.23.0',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'Postman-Token': 'f6b7900a-c687-405d-a3f6-5467018c736b',
        'Host': 'devapi.ed.rt.ru',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'JSESSIONID=4476582DF6A963142434BCDCF3AACCE1',
        'Content-Length': '470',
        'Connection': 'keep-alive'
    }

    headers2 = {
        'Authorization': 'Basic ZWRfcWFfdGVzdDpDZTFCJFRNc1ZFaU0=',
        'User-Agent': 'PostmanRuntime/7.23.0',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'Postman-Token': 'f6b7900a-c687-405d-a3f6-5467018c736b',
        'Host': 'devapi.ed.rt.ru',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'JSESSIONID=4476582DF6A963142434BCDCF3AACCE1',
        'Content-Length': '470',
        'Connection': 'keep-alive'
    }

    headers1 = {
        'Authorization': 'Basic ZWRfdXJhbF90ZXN0OmJ+VHkzYXRub2d7V3hEayM='
    }

    data_download = \
        [{"type": "EDOCONTRACT", "link": "http://10.42.110.215:8010/file?id=edocontract.pdf", "displayName": "ALIANCE"}]
