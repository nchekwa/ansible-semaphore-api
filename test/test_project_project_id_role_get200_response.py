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

from semaphore_api.models.project_project_id_role_get200_response import ProjectProjectIdRoleGet200Response

class TestProjectProjectIdRoleGet200Response(unittest.TestCase):
    """ProjectProjectIdRoleGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectProjectIdRoleGet200Response:
        """Test ProjectProjectIdRoleGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectProjectIdRoleGet200Response`
        """
        model = ProjectProjectIdRoleGet200Response()
        if include_optional:
            return ProjectProjectIdRoleGet200Response(
                role = 'owner',
                permissions = 0.0
            )
        else:
            return ProjectProjectIdRoleGet200Response(
        )
        """

    def testProjectProjectIdRoleGet200Response(self):
        """Test ProjectProjectIdRoleGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
