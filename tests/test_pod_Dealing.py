# coding=utf-8
from __future__ import unicode_literals
import random
import string
import unittest

from pod_base import InvalidDataException, APIException

from tests.config import *
from pod_dealing import PodDealing
from uuid import uuid4
from datetime import datetime


class TestPodDealing(unittest.TestCase):
    __slots__ = ("__dealing", "__letters", "__dealer_id", "__dealer_api_token", "__dealing_dealer")

    def setUp(self):
        self.__dealing = PodDealing(api_token=API_TOKEN, server_type=SERVER_MODE)
        self.__letters = string.ascii_lowercase[:12]
        self.__dealer_id = 14589  # default

    def __random_string(self, length=15):
        return "".join(random.choice(self.__letters) for i in range(length))

    def test_1_add_user_and_business_required_params(self):
        username = "test_py_user_{}".format(str(uuid4()).replace("-", "_"))
        email = "{}@pytest.pytest".format(self.__random_string())
        business_name = "کسب و کار پایتونی {}".format((datetime.now()).__format__("%Y%m%d%H%M%S"))
        result = self.__dealing.add_user_and_business(username=username, agent_cellphone_number=AGENT_CELLPHONE_NUMBER,
                                                      agent_first_name=AGENT_FIRST_NAME,
                                                      agent_last_name=AGENT_LAST_NAME,
                                                      description="ایجاد توسط تست SDK پایتون", email=email,
                                                      guild_code=["API_GUILD", "CLOTHING_GUILD"],
                                                      business_name=business_name, country="ایران", state="خراسان رضوی",
                                                      city="مشهد", address="فناپ سافت مشهد")

        self.assertIsInstance(result, dict)

    def test_1_add_user_and_business_full_params(self):
        username = "test_py_user_{}".format(str(uuid4()).replace("-", "_"))
        email = "{}@pytest.pytest".format(self.__random_string())
        business_name = "کسب و کار پایتونی {}".format((datetime.now()).__format__("%Y%m%d%H%M%S"))
        national_code = "{}{}".format(random.randint(1000000, 9999999), random.randint(1000, 9999))

        other_params = {
            "firstName": "FIRST NAME",
            "lastName": "LAST NAME",
            "sheba": "980570100680013557234101",
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
            "link": "LINK",
            "lat": 35.12345,
            "lng": 35.12345,
            "agentNationalCode": "1111221111",
        }

        result = self.__dealing.add_user_and_business(username=username, agent_cellphone_number=AGENT_CELLPHONE_NUMBER,
                                                      agent_first_name=AGENT_FIRST_NAME,
                                                      agent_last_name=AGENT_LAST_NAME,
                                                      description="ایجاد توسط تست SDK پایتون", email=email,
                                                      guild_code=["API_GUILD", "CLOTHING_GUILD"],
                                                      business_name=business_name, country="ایران", state="خراسان رضوی",
                                                      city="مشهد", address="فناپ سافت مشهد", **other_params
                                                      )

        self.assertIsInstance(result, dict)
        self.__dealer_id = result["id"]

    def test_1_add_user_and_business_validation_error(self):
        username = "reza1607"
        email = "abcd"
        business_name = "کسب و کار پایتونی"

        with self.assertRaises(InvalidDataException, msg="خطای اعتبار سنجی"):
            self.__dealing.add_user_and_business(username=username, agent_cellphone_number=AGENT_CELLPHONE_NUMBER,
                                                 agent_first_name=AGENT_FIRST_NAME,
                                                 agent_last_name=AGENT_LAST_NAME,
                                                 description="ایجاد توسط تست SDK پایتون", email=email,
                                                 guild_code=["API_GUILD", "CLOTHING_GUILD"],
                                                 business_name=business_name, country="ایران", state="خراسان رضوی",
                                                 city="مشهد", address="فناپ سافت مشهد")

    def test_2_update_business_required_params(self):
        result = self.__dealing.update_business(self.__dealer_id, business_name="Edited",
                                                description="کسب و کار ویرایشی",
                                                guild_code=["API_GUILD", "CLOTHING_GUILD",
                                                            "INFORMATION_TECHNOLOGY_GUILD"],
                                                country="ایران", state="خراسان رضوی", city="مشهد",
                                                address="فناپ سافت مشهد - ویرایش شده")
        self.assertIsInstance(result, dict)

    def test_2_update_business_full_params(self):
        national_code = "{}{}".format(random.randint(1000000, 9999999), random.randint(1000, 9999))

        other_params = {
            "firstName": "FIRST NAME",
            "lastName": "LAST NAME",
            "email": "t@t.com",
            "companyName": "فناپ کشت گر",  # نام شرکت
            "sheba": "980570100680013557234101",
            "shopName": "فروشگاه مرکزی",
            "shopNameEn": "Shopping Center",  # نام انگلیسی فروشگاه
            "dateEstablishing": "1398/01/27",  # تاریخ شمسی تاسیس yyyy/mm/dd
            "website": "website",  # وبسایت
            "nationalCode": national_code,
            "economicCode": "123",
            "registrationNumber": "1234fa",
            "cellphone": "09150000000",
            "phone": "05132222222",
            "fax": "05133333333",
            "postalCode": "9185175673",
            "changeLogo": True,  # در صورتی که بخواهید تصویر لوگو را تغییر دهید True وارد کنید
            "changeCover": True,  # در صورتی که بخواهید تصویر کاور را تغییر دهید True وارد کنید
            "logoImage": "https://30secondsofknowledge.com/static/media/logo_light.b1bd345c.png",
            "coverImage": "https://30secondsofknowledge.com/static/media/mockup.71757ecc.jpg",
            "tags": "TAG1,TAG2",
            # "tagTrees"              : ["TestTagCategory5dbfefe86b953"],
            # "tagTreeCategoryName": "TestTagCategory5dc12fabea220",
            "link": "http://karthing.ir",
            "lat": 35.12345,
            "lng": 35.12345,
            "agentFirstName": "FIRST NAME",  # نام نماینده
            "agentLastName": "LAST NAME",  # نام خانوادگی نماینده
            "agentCellphoneNumber": "MOBILE",  # شماره تلفن نماینده
            "agentNationalCode": "1111221111"
        }

        result = self.__dealing.update_business(self.__dealer_id, business_name="Edited",
                                                description="کسب و کار ویرایشی",
                                                guild_code=["API_GUILD", "CLOTHING_GUILD",
                                                            "INFORMATION_TECHNOLOGY_GUILD"],
                                                country="ایران", state="خراسان رضوی", city="مشهد",
                                                address="فناپ سافت مشهد - ویرایش شده", **other_params)
        self.assertIsInstance(result, dict)

    def test_2_update_business_validation_error(self):
        with self.assertRaises(InvalidDataException):
            other_params = {
                "email": "abcde"
            }

            self.__dealing.update_business(self.__dealer_id, business_name="Edited",
                                           description="کسب و کار ویرایشی",
                                           guild_code=["API_GUILD", "CLOTHING_GUILD", "INFORMATION_TECHNOLOGY_GUILD"],
                                           country="ایران", state="خراسان رضوی", city="مشهد",
                                           address="فناپ سافت مشهد - ویرایش شده", **other_params)

    def test_3_list_user_created_business(self):
        businesses = self.__dealing.list_user_created_business()
        self.assertIsInstance(businesses, list)

    def test_3_list_user_created_business_filter_by_biz_id(self):
        params = {
            "bizId": [self.__dealer_id]
        }

        businesses = self.__dealing.list_user_created_business(**params)
        self.assertIsInstance(businesses, list)
        self.assertEqual(len(businesses), 1)
        self.assertEqual(businesses[0]["id"], self.__dealer_id)

    def test_3_list_user_created_business_filter_by_biz_id_not_exists(self):
        params = {
            "bizId": [-1]
        }

        businesses = self.__dealing.list_user_created_business(**params)
        self.assertIsInstance(businesses, list)
        self.assertEqual(len(businesses), 0)

    def test_3_list_user_created_business_validation_error(self):
        params = {
            "bizId": "this is a string"
        }

        with self.assertRaises(InvalidDataException):
            self.__dealing.list_user_created_business(**params)

    def test_4_get_api_token_for_created_business(self):
        result = self.__dealing.get_api_token_for_created_business(business_id=self.__dealer_id)
        self.assertIsInstance(result, dict)
        self.__dealer_api_token = result["apiToken"]

    def create_dealing_dealer(self):
        self.__dealing = PodDealing(api_token=self.__dealer_api_token, server_type=SERVER_MODE)

    def test_4_get_api_token_for_created_business_biz_id_not_exists(self):
        with self.assertRaises(APIException):
            self.__dealing.get_api_token_for_created_business(business_id=-1)

    def test_4_get_api_token_for_created_business_validation_error(self):
        with self.assertRaises(TypeError):
            self.__dealing.get_api_token_for_created_business()

    def test_5_favorite_business(self):
        self.assertEqual(self.__dealing.favorite_business(self.__dealer_id), True)

    def test_5_favorite_business_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.assertEqual(self.__dealing.favorite_business("biz id"), True)

    def test_5_favorite_business_biz_id_not_exists(self):
        with self.assertRaises(APIException):
            self.__dealing.favorite_business(-1)

    # def test_6_rate_business(self):
    #     self.assertEqual(self.__dealing.rate_business(self.__dealer_id, 5), True)

    def test_6_rate_business_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.assertEqual(self.__dealing.rate_business("biz id", 9), True)

    def test_6_rate_business_biz_id_not_exists(self):
        with self.assertRaises(APIException):
            self.__dealing.rate_business(-1, 5)

    def test_7_comment_business(self):
        self.assertGreaterEqual(self.__dealing.comment_business(self.__dealer_id, "این یک نظر از سمت تست پایتون است"),
                                1, msg="send comment : successful comment")

    def test_7_comment_business_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="send comment : invalid param"):
            self.__dealing.comment_business(-1, 54654)

    def test_7_comment_business_biz_id_not_exists(self):
        with self.assertRaises(APIException, msg="send comment : business not exists"):
            self.__dealing.comment_business(-1, "این یک نظر از سمت تست پایتون است")

    def test_8_comment_business_list(self):
        result = self.__dealing.comment_business_list(self.__dealer_id)
        self.assertIsInstance(result, list, msg="comment list : check instance")
        self.assertGreaterEqual(len(result), 1, msg="comment list : check len")

    def test_8_comment_business_list_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="comment list : invalid param"):
            self.__dealing.comment_business_list("biz id")

    def test_8_comment_business_list_required_params(self):
        with self.assertRaises(TypeError, msg="comment list : required params"):
            self.__dealing.comment_business_list()

    def test_8_comment_business_list_first_id(self):
        self.__dealing.comment_business_list(self.__dealer_id, firstId=0, msg="comment list : set first id")

    def test_8_comment_business_list_last_id(self):
        self.__dealing.comment_business_list(self.__dealer_id, lastId=0, msg="comment list : set last id")

    def test_9_confirm_comment(self):
        comments = self.__dealing.comment_business_list(BUSINESS_ID)
        self.assertEqual(self.__dealing.confirm_comment(comments[0]["id"]), True, msg="confirm comment : success")

    def test_9_confirm_comment_required_params(self):
        with self.assertRaises(TypeError, msg="confirm comment : require params"):
            self.__dealing.confirm_comment()

    def test_10_un_confirm_comment(self):
        comments = self.__dealing.comment_business_list(BUSINESS_ID)
        self.assertEqual(self.__dealing.un_confirm_comment(comments[0]["id"]), True, msg="unconfirm comment : success")

    def test_10_un_confirm_comment_required_params(self):
        with self.assertRaises(TypeError, msg="unconfirm comment : require params"):
            self.__dealing.un_confirm_comment()

    def test_11_dis_favorite_business(self):
        self.assertEqual(self.__dealing.dis_favorite_business(self.__dealer_id), True,
                         msg="dis favorite : successful dis favorite")

    def test_11_dis_favorite_business_validation_error(self):
        with self.assertRaises(TypeError, msg="dis favorite : invalid param"):
            self.__dealing.dis_favorite_business()

    def test_11_dis_favorite_business_biz_id_not_exists(self):
        with self.assertRaises(APIException, msg="dis favorite : business not exists"):
            self.__dealing.dis_favorite_business(-1)

    def test_12_user_business_infos(self):
        result = self.__dealing.user_business_infos([self.__dealer_id])
        self.assertIsInstance(result, list, msg="user business infos : check instance")
        self.assertEqual(len(result), 1, msg="user business infos : check len")

    def test_12_user_business_infos_required_params(self):
        with self.assertRaises(TypeError, msg="user business infos : required params"):
            self.__dealing.user_business_infos()

    def test_12_user_business_infos_validation_error_params(self):
        with self.assertRaises(InvalidDataException, msg="user business infos : invalid param"):
            self.__dealing.user_business_infos(["biz id1", "biz id2"])

    def test_12_user_business_infos_biz_id_not_exists(self):
        result = self.__dealing.user_business_infos([-1])
        self.assertIsInstance(result, list, msg="user business infos : not exists - check instance")
        self.assertEqual(len(result), 0, msg="user business infos : not exists - check len")

    def test_13_add_dealer(self):
        result = self.__dealing.add_dealer(dealer_biz_id=self.__dealer_id, all_product_allow=True)
        self.assertEqual(result["dealer"]["id"], self.__dealer_id, msg="add dealer : check business id dealer")
        self.assertEqual(result["allProductAllow"], True, msg="add dealer: check all product allow")

    def test_13_add_dealer_all_params(self):
        result = self.__dealing.add_dealer(dealer_biz_id=self.__dealer_id,
                                           all_product_allow=True,
                                           sc_api_key=SC_API_KEY,
                                           sc_voucher_hash=SC_VOUCHER_HASH)
        self.assertEqual(result["dealer"]["id"], self.__dealer_id,
                         msg="add dealer : check business id dealer (all params)")
        self.assertEqual(result["allProductAllow"], True, msg="add dealer: check all product allow (all params)")

    def test_13_add_dealer_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="add dealer : validation error"):
            self.__dealing.add_dealer("biz id")

    def test_13_add_dealer_required_params(self):
        with self.assertRaises(TypeError, msg="add dealer : required params"):
            self.__dealing.add_dealer()

    def test_14_dealer_list(self):
        dealers = self.__dealing.dealer_list()
        self.assertIsInstance(dealers, list, msg="dealer list : check instance")
        self.assertGreaterEqual(len(dealers), 1, msg="dealer list : check len")

    def test_14_dealer_list_validation_error(self):
        with self.assertRaises(InvalidDataException):
            self.__dealing.dealer_list(dealerBizId="asdasd")

    def test_14_dealer_list_all_params(self):
        dealers = self.__dealing.dealer_list(page=1, size=50, enable=True, dealerBizId=self.__dealer_id)
        self.assertIsInstance(dealers, list, msg="dealer list : check instance")
        self.assertGreaterEqual(len(dealers), 0, msg="dealer list : check len")
        if len(dealers):
            self.assertGreaterEqual(dealers[0]["dealer"]["id"], self.__dealer_id,
                                    msg="dealer list : check dealer biz id")

    def test_15_enable_dealer(self):
        result = self.__dealing.enable_dealer(self.__dealer_id)
        self.assertIsInstance(result, dict, msg="enable dealer : check instance")
        self.assertEqual(result["dealer"]["id"], self.__dealer_id, msg="enable dealer : check dealer biz id")
        self.assertEqual(result["enable"], True, msg="disable dealer : check status")

    def test_15_enable_dealer_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="enable dealer : validation error"):
            self.__dealing.enable_dealer("biz id")

    def test_15_enable_dealer_required_params(self):
        with self.assertRaises(TypeError, msg="enable dealer : required params"):
            self.__dealing.enable_dealer()

    def test_15_disable_dealer(self):
        result = self.__dealing.disable_dealer(self.__dealer_id)
        self.assertIsInstance(result, dict, msg="disable dealer : check instance")
        self.assertEqual(result["dealer"]["id"], self.__dealer_id, msg="disable dealer : check dealer biz id")
        self.assertEqual(result["enable"], False, msg="disable dealer : check status")

    def test_15_disable_dealer_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="disable dealer : validation error"):
            self.__dealing.disable_dealer("biz id")

    def test_15_disable_dealer_required_params(self):
        with self.assertRaises(TypeError, msg="disable dealer : required params"):
            self.__dealing.disable_dealer()

    def test_16_business_dealing_list(self):
        dealings = self.__dealing.business_dealing_list()
        self.assertIsInstance(dealings, list, msg="business dealing list : check instance")
        self.assertGreaterEqual(len(dealings), 1, msg="business dealing list : check len")

    def test_16_business_dealing_list_all_params(self):
        dealings = self.__dealing.business_dealing_list(dealingBusinessId=self.__dealer_id, enable=True)
        self.assertIsInstance(dealings, list, msg="business dealing list : check instance")
        self.assertGreaterEqual(len(dealings), 0, msg="business dealing list : check len")

    def test_17_add_dealer_product_permission_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="add dealer product permission : validation error"):
            self.__dealing.add_dealer_product_permission("biz id", "product id")

    def test_17_add_dealer_product_permission_required_params(self):
        with self.assertRaises(TypeError, msg="add dealer product permission : required params"):
            self.__dealing.add_dealer_product_permission()

    def test_18_dealer_product_permission_list(self):
        permissions = self.__dealing.dealer_product_permission_list()
        self.assertIsInstance(permissions, list, msg="dealer product permission list : check instance")
        self.assertGreaterEqual(len(permissions), 0, msg="dealer product permission list : check len")

    def test_18_dealer_product_permission_list_validation_error(self):
        with self.assertRaises(TypeError, msg="add dealer product permission : validation error"):
            self.__dealing.dealer_product_permission_list("page 1", "size 20")

        with self.assertRaises(InvalidDataException, msg="add dealer product permission : validation error"):
            self.__dealing.dealer_product_permission_list(dealerBizId="biz id")

    def test_19_enable_dealer_product_permission(self):
        permissions = self.__dealing.dealer_product_permission_list()
        if len(permissions) == 0:
            return

        result = self.__dealing.enable_dealer_product_permission(product_id=permissions[0]["product"]["entityId"],
                                                                 dealer_biz_id=
                                                                 permissions[0]["businessDealer"]["dealer"]["id"])

        self.assertIsInstance(result, dict, msg="enable dealer product permission : check instance")
        self.assertEqual(result["enable"], True, msg="enable dealer product permission : check status")

    def test_19_enable_dealer_product_permission_required_params(self):
        with self.assertRaises(TypeError, msg="enable dealer product permission : required params"):
            self.__dealing.enable_dealer_product_permission()

    def test_19_enable_dealer_product_permission_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="enable dealer product permission : validation error"):
            self.__dealing.enable_dealer_product_permission(product_id="abcd", dealer_biz_id="biz id")

    def test_20_disable_dealer_product_permission(self):
        permissions = self.__dealing.dealer_product_permission_list()
        if len(permissions) == 0:
            return

        result = self.__dealing.disable_dealer_product_permission(product_id=permissions[0]["product"]["entityId"],
                                                                  dealer_biz_id=
                                                                  permissions[0]["businessDealer"]["dealer"]["id"])

        self.assertIsInstance(result, dict, msg="disable dealer product permission : check instance")
        self.assertEqual(result["enable"], False, msg="disable dealer product permission : check status")

    def test_20_disable_dealer_product_permission_required_params(self):
        with self.assertRaises(TypeError, msg="disable dealer product permission : required params"):
            self.__dealing.disable_dealer_product_permission()

    def test_20_disable_dealer_product_permission_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="disable dealer product permission : validation error"):
            self.__dealing.disable_dealer_product_permission(product_id="abcd", dealer_biz_id="biz id")
