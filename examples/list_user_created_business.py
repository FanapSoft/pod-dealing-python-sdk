# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    params = {
        # "bizId": [14592, 14590, 14589],
        # "guildCode": ["API_GUILD", "CLOTHING_GUILD"],
        # "query": "پایتون",
        # "username": 'USER NAME',
        "businessName": 'کسب و کار پایتونی 20200115133012',
        # "email": 'EMAIL',
        # "country": 'COUNTRY',
        # "state": 'STATE',
        # "city": 'CITY',
        # "active": True,
        # "size": 50,
        # "ssoId": 'SSO ID',  # شناسه sso کاربر
        # "sheba": 'SHEBA WITHOUT IR',
        # "nationalCode": 'CODE',
        # "economicCode": 'CODE',
        # "cellphone": '09120000000',
        # "tags": 'TAG1,TAG2',  # لیست تگ
        # "tagTrees": 'TREE1,TREE2',  # لیست درخت تگ
        # "sc_api_key": SC_API_KEY,
        # "sc_voucher_hash": SC_VOUCHER_HASH
    }

    print("Businesses\n", pod_dealing.list_user_created_business(**params))
    print("Total :", pod_dealing.total_items())
    # OUTPUT
    # Businesses
    # [
    #  {
    #     "id": 14589,
    #     "name": "کسب و کار پایتونی 20200115133012",
    #     "guilds": [
    #       {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       {
    #         "id": 52,
    #         "name": "پوشاک",
    #         "code": "CLOTHING_GUILD"
    #       }
    #     ],
    #     "description": "ایجاد توسط تست SDK پایتون",
    #     "image": "LOGO",
    #     "coverImage": "COVER",
    #     "address": "فناپ سافت مشهد",
    #     "city": "مشهد",
    #     "state": "خراسان رضوی",
    #     "country": "ایران",
    #     "postalcode": "9185175673",
    #     "phone": "05132222222",
    #     "cellphone": "09150000000",
    #     "faxNumber": "05133333333",
    #     "latitude": 35.12345,
    #     "longitude": 35.12345,
    #     "subscriptionCount": 0,
    #     "subscribed": false,
    #     "numOfComments": 0,
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     },
    #     "userId": 31703,
    #     "ssoId": "17406108",
    #     "numOfProducts": 0,
    #     "firstName": "FIRST NAME",
    #     "lastName": "LAST NAME",
    #     "nationalCode": "31145089447",
    #     "economicCode": "123",
    #     "registrationNumber": "1234fa",
    #     "sheba": "980500000000000000000101",
    #     "email": "jcabdbefddiljli@pytest.pytest",
    #     "fullAddress": "ایران-خراسان رضوی-مشهد-فناپ سافت مشهد",
    #     "tags": [
    #       "TAG1"
    #     ],
    #     "tagTrees": [],
    #     "link": "LINK",
    #     "active": false,
    #     "agent": {
    #       "id": 7450,
    #       "firstName": "رضا",
    #       "lastName": "زارع",
    #       "cellphoneNumber": "09370000041",
    #       "nationalCode": "1111221111"
    #     },
    #     "numOfLike": 0,
    #     "numOfDislike": 0,
    #     "username": "test_py_user_55bc3f61_1df7_41ac_8d05_974b7c177224",
    #     "creator": {
    #       "id": 16128,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     }
    #   },
    #   ...
    # ]
    # Total : 1
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
