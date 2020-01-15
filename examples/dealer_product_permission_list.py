# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dealing.dealer_product_permission_list(sc_api_key=SC_API_KEY, sc_voucher_hash=SC_VOUCHER_HASH))
    print("Total :", pod_dealing.total_items())
    # OUTPUT
    # [
    #  {
    #     "product": {
    #       "id": 0,
    #       "version": 68,
    #       "timelineId": 0,
    #       "entityId": 29990,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 0,
    #       "enable": False,
    #       "hide": False,
    #       "business": {
    #         "id": 7867,
    #         "name": "شرکت رضا",
    #         "numOfProducts": 369,
    #         "rate": {
    #           "rate": 8,
    #           "rateCount": 1
    #         },
    #         "sheba": "640170000000000000000007"
    #       },
    #       "latitude": 0,
    #       "longitude": 0,
    #       "name": "ویرایش محصول تست کیس",
    #       "description": "ویرایش محصول",
    #       "categoryList": [],
    #       "preview": "True",
    #       "unlimited": True,
    #       "availableCount": 0,
    #       "price": 40000,
    #       "discount": 0,
    #       "rate": {
    #         "rate": 0,
    #         "rateCount": 0
    #       },
    #       "attributeValues": [
    #         {
    #           "code": "gender",
    #           "name": "جنسیت",
    #           "value": "مرد"
    #         },
    #         {
    #           "code": "size",
    #           "name": "اندازه",
    #           "value": "XL"
    #         },
    #         {
    #           "code": "color",
    #           "name": "رنگ",
    #           "value": "سفید"
    #         }
    #       ],
    #       "allowUserInvoice": False,
    #       "allowUserPrice": False,
    #       "templateCode": "پیراهن مردانه",
    #       "productGroup": {
    #         "id": 1921,
    #         "sharedAttributeCodes": [
    #           "color",
    #           "size"
    #         ]
    #       },
    #       "currency": {
    #         "name": "ریال",
    #         "code": "IRR"
    #       }
    #     },
    #     "businessDealer": {
    #       "business": {
    #         "id": 7867,
    #         "name": "شرکت رضا",
    #         "numOfProducts": 369,
    #         "rate": {
    #           "rate": 8,
    #           "rateCount": 1
    #         },
    #         "sheba": "640170000000000000000007"
    #       },
    #       "dealer": {
    #         "id": 9371,
    #         "name": "رضا استور شماره 7",
    #         "numOfProducts": 103,
    #         "rate": {
    #           "rate": 0,
    #           "rateCount": 0
    #         }
    #       },
    #       "enable": True,
    #       "allProductAllow": False
    #     },
    #     "enable": True
    #   },
    #  ...
    # ]
    # Total : 3

except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
