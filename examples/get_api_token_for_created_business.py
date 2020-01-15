# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dealing.get_api_token_for_created_business(business_id=9371, sc_api_key=SC_API_KEY,
                                                         sc_voucher_hash=SC_VOUCHER_HASH))
    # OUTPUT
    # {
    #   "business": {
    #     "id": 9371,
    #     "name": "رضا استور شماره 7",
    #     "numOfProducts": 103,
    #     "rate": {
    #       "rate": 0,
    #       "rateCount": 0
    #     }
    #   },
    #   "apiToken": "a13f9xxxxxxxxxxxxxxxxxxxxxxxxc0f",
    #   "clientId": "9327xxxxxxxxxxxxxxxxxx76"
    # }
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
