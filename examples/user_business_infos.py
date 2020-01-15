# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_dealing import PodDealing

try:
    pod_dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
    print(pod_dealing.user_business_infos(business_ids=[9371], sc_api_key=SC_API_KEY,
                                          sc_voucher_hash=SC_VOUCHER_HASH))
    # OUTPUT
    # [
    #  {
    #   'id': 9371,
    #   'name': 'رضا استور شماره 7',
    #   'subscriptionCount': 7,
    #   'subscribed': False,
    #   'rate': {
    #       'rate': 0.0,
    #       'rateCount': 0
    #   },
    #   'favorite': False
    #   },
    # ...
    # ]
except APIException as e:
    print("API Exception\nError {}\nReference Number : {}".format(e.message, e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
