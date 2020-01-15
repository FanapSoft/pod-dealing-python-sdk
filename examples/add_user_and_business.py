# coding=utf-8
from __future__ import unicode_literals

import random
import string
from datetime import datetime
from uuid import uuid4

from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing


def random_string(length=15):
    letters = string.ascii_lowercase[:12]
    return "".join(random.choice(letters) for i in range(length))


try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)

    username = "test_py_user_{}".format(str(uuid4()).replace("-", "_"))
    email = "{}@pytest.pytest".format(random_string())
    national_code = "{}{}".format(random.randint(1000000, 9999999), random.randint(1000, 9999))
    business_name = "کسب و کار پایتونی {}".format((datetime.now()).__format__("%Y%m%d%H%M%S"))

    params = {
        "firstName": "FIRST NAME",
        "lastName": "LAST NAME",
        "sheba": "980570100000000000000101",
        "nationalCode": national_code,
        "economicCode": "123",
        "registrationNumber": "1234fa",
        "cellphone": "09150000000",
        "phone": "05132222222",
        "fax": "05133333333",
        "postalCode": "9185175673",
        "newsReader": True,
        "logoImage": "LOGO",
        "coverImage": "COVER",
        "tags": "TAG1,TAG2",
        # "tagTrees": "TestTagCategory5dbfefe86b953",
        # "tagTreeCategoryName": "TestTagCategory5dc12fabea220",
        "link": "http://google.com",
        "lat": 35.12345,
        "lng": 35.12345,
        "agentNationalCode": "1111221111",

    }

    AGENT_CELLPHONE_NUMBER = "09370000041"
    AGENT_FIRST_NAME = "رضا"
    AGENT_LAST_NAME = "زارع"

    print(pod_dealing.add_user_and_business(username=username, agent_cellphone_number=AGENT_CELLPHONE_NUMBER,
                                            agent_first_name=AGENT_FIRST_NAME,
                                            agent_last_name=AGENT_LAST_NAME,
                                            description="ایجاد توسط تست SDK پایتون", email=email,
                                            guild_code=["API_GUILD", "CLOTHING_GUILD"],
                                            business_name=business_name, country="ایران", state="خراسان رضوی",
                                            city="مشهد", address="فناپ سافت مشهد", **params
                                            ))

    # OUTPUT
    # {
    #   "id": 14592,
    #   "name": "کسب و کار پایتونی 20200115133724",
    #   "guilds": [
    #     {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     {
    #       "id": 52,
    #       "name": "پوشاک",
    #       "code": "CLOTHING_GUILD"
    #     }
    #   ],
    #   "description": "ایجاد توسط تست SDK پایتون",
    #   "image": "LOGO",
    #   "coverImage": "COVER",
    #   "address": "فناپ سافت مشهد",
    #   "city": "مشهد",
    #   "state": "خراسان رضوی",
    #   "country": "ایران",
    #   "postalcode": "9185175673",
    #   "phone": "05132222222",
    #   "cellphone": "09150000000",
    #   "faxNumber": "05133333333",
    #   "latitude": 35.12345,
    #   "longitude": 35.12345,
    #   "subscriptionCount": 0,
    #   "subscribed": False,
    #   "numOfComments": 0,
    #   "rate": {
    #     "rate": 0,
    #     "rateCount": 0
    #   },
    #   "userId": 31706,
    #   "ssoId": "17406132",
    #   "numOfProducts": 0,
    #   "firstName": "FIRST NAME",
    #   "lastName": "LAST NAME",
    #   "nationalCode": "16680907544",
    #   "economicCode": "123",
    #   "registrationNumber": "1234fa",
    #   "sheba": "980570100000000000000101",
    #   "email": "beelhhgcdgaahga@pytest.pytest",
    #   "fullAddress": "ایران-خراسان رضوی-مشهد-فناپ سافت مشهد",
    #   "tags": [
    #     "TAG1"
    #   ],
    #   "tagTrees": [],
    #   "link": "http://google.com",
    #   "active": False,
    #   "apiToken": "248518f5381045acb6345a213a87f728",
    #   "agent": {
    #     "id": 7453,
    #     "firstName": "رضا",
    #     "lastName": "زارع",
    #     "cellphoneNumber": "09370000041",
    #     "nationalCode": "1111221111"
    #   },
    #   "numOfLike": 0,
    #   "numOfDislike": 0,
    #   "username": "test_py_user_574532aa_a8b2_4481_814d_a821a69dbdef",
    #   "creator": {
    #     "id": 16128,
    #     "name": "شرکت رضا زارع",
    #     "ssoId": "11963175",
    #     "ssoIssuerCode": 1,
    #     "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #   }
    # }
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
