# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    params = {
        # "dealingBusinessId": 12006,
        # "enable": True,
        # "sc_api_key": SC_API_KEY,
        # "sc_voucher_hash": SC_VOUCHER_HASH
    }

    print("Businesses\n", pod_dealing.business_dealing_list(**params))
    print("Total :", pod_dealing.total_items())
    # OUTPUT
    # Businesses
    # [
    #   {
    #     "business": {
    #       "id": 12006,
    #       "name": "Fanap",
    #       "numOfProducts": 15,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "sheba": "210150000000000000000010"
    #     },
    #     "dealer": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 369,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000007"
    #     },
    #     "enable": True,
    #     "allProductAllow": True
    #   },
    #   ...
    # ]
    # Total : 4
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
