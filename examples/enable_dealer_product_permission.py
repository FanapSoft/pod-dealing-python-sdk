# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dealing.enable_dealer_product_permission(dealer_biz_id=12006, product_id=45898, sc_api_key=SC_API_KEY,
                                                        sc_voucher_hash=SC_VOUCHER_HASH))
    # OUTPUT
    # {
    #   "product": {
    #     "id": 0,
    #     "version": 2,
    #     "timelineId": 0,
    #     "entityId": 45898,
    #     ...
    #     "preferredTaxRate": 0
    #   },
    #   "businessDealer": {
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 369,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000007"
    #     },
    #     "dealer": {
    #       "id": 12006,
    #       "name": "Fanap",
    #       "numOfProducts": 15,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "sheba": "210150000000000000000010"
    #     },
    #     "enable": True,
    #     "allProductAllow": True
    #   },
    #   "enable": True
    # }

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
