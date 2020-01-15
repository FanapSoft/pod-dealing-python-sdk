# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print("Dealers\n", pod_dealing.dealer_list(sc_api_key=SC_API_KEY, sc_voucher_hash=SC_VOUCHER_HASH))
    print("Total Dealers :", pod_dealing.total_items())
    # OUTPUT
    # Dealers
    # [
    #   {
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 369,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000002007"
    #     },
    #     "dealer": {
    #       "id": 8821,
    #       "name": "خدمات رفاهی آوند",
    #       "image": "https://core.pod.ir:443/nzh/image/?imageId=...",
    #       "numOfProducts": 3,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "sheba": "970570000000000002000604"
    #     },
    #     "enable": True,
    #     "allProductAllow": True
    #   },
    #   ...
    # ]
    # Total Dealers : 6
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
