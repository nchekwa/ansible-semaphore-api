# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from semaphore_api.models.users_user_id_password_post_request import UsersUserIdPasswordPostRequest

class TestUsersUserIdPasswordPostRequest(unittest.TestCase):
    """UsersUserIdPasswordPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsersUserIdPasswordPostRequest:
        """Test UsersUserIdPasswordPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersUserIdPasswordPostRequest`
        """
        model = UsersUserIdPasswordPostRequest()
        if include_optional:
            return UsersUserIdPasswordPostRequest(
                password = ''
            )
        else:
            return UsersUserIdPasswordPostRequest(
        )
        """

    def testUsersUserIdPasswordPostRequest(self):
        """Test UsersUserIdPasswordPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
