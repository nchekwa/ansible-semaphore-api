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

from semaphore_api.models.login_metadata import LoginMetadata

class TestLoginMetadata(unittest.TestCase):
    """LoginMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginMetadata:
        """Test LoginMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginMetadata`
        """
        model = LoginMetadata()
        if include_optional:
            return LoginMetadata(
                oidc_providers = [
                    semaphore_api.models.login_metadata_oidc_providers_inner.LoginMetadata_oidc_providers_inner(
                        id = '', 
                        name = '', )
                    ]
            )
        else:
            return LoginMetadata(
        )
        """

    def testLoginMetadata(self):
        """Test LoginMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
