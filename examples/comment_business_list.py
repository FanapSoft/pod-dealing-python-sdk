# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dealing.comment_business_list(business_id=9371, sc_api_key=SC_API_KEY, sc_voucher_hash=SC_VOUCHER_HASH))
    # OUTPUT
    # [
    #   {
    #     "id": 7842,
    #     "text": "ثبت نظر تستی",
    #     "timestamp": 1579005007189,
    #     "user": {
    #       "id": 16128,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "confirmed": False,
    #     "numOfLikes": 0,
    #     "numOfComments": 0,
    #     "liked": False
    #   },
    #   {
    #     "id": 7841,
    #     "text": "ثبت نظر تستی",
    #     "timestamp": 1579004878813,
    #     "user": {
    #       "id": 16128,
    #       "name": "شرکت رضا زارع",
    #       "ssoId": "11963175",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     },
    #     "confirmed": False,
    #     "numOfLikes": 0,
    #     "numOfComments": 0,
    #     "liked": False
    #   }
    # ]
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
