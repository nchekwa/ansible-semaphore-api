# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.access_key_request import AccessKeyRequest

class TestAccessKeyRequest(unittest.TestCase):
    """AccessKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessKeyRequest:
        """Test AccessKeyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessKeyRequest`
        """
        model = AccessKeyRequest()
        if include_optional:
            return AccessKeyRequest(
                name = 'None',
                type = 'none',
                project_id = 1,
                login_password = semaphore_api.models.access_key_request_login_password.AccessKeyRequest_login_password(
                    password = 'password', 
                    login = 'username', ),
                ssh = semaphore_api.models.access_key_request_ssh.AccessKeyRequest_ssh(
                    login = 'user', 
                    private_key = 'private key', )
            )
        else:
            return AccessKeyRequest(
        )
        """

    def testAccessKeyRequest(self):
        """Test AccessKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
