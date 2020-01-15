# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dealing.add_dealer(dealer_biz_id=12006, all_product_allow=False, sc_api_key=SC_API_KEY,
                                 sc_voucher_hash=SC_VOUCHER_HASH))

    # OUTPUT
    # {
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
    #       "id": 12006,
    #       "name": "Fanap",
    #       "image": "https://core.pod.ir:443/nzh/image/?imageId=...",
    #       "numOfProducts": 3,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "sheba": "970570000000000000000004"
    #     },
    #     "enable": True,
    #     "allProductAllow": False
    #   }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
