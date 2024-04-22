# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.integration_request import IntegrationRequest

class TestIntegrationRequest(unittest.TestCase):
    """IntegrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IntegrationRequest:
        """Test IntegrationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IntegrationRequest`
        """
        model = IntegrationRequest()
        if include_optional:
            return IntegrationRequest(
                name = 'deploy',
                project_id = 56,
                template_id = 56
            )
        else:
            return IntegrationRequest(
        )
        """

    def testIntegrationRequest(self):
        """Test IntegrationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
