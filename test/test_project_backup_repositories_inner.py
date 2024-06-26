# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.project_backup_repositories_inner import ProjectBackupRepositoriesInner

class TestProjectBackupRepositoriesInner(unittest.TestCase):
    """ProjectBackupRepositoriesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBackupRepositoriesInner:
        """Test ProjectBackupRepositoriesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBackupRepositoriesInner`
        """
        model = ProjectBackupRepositoriesInner()
        if include_optional:
            return ProjectBackupRepositoriesInner(
                name = '',
                git_url = '',
                git_branch = '',
                ssh_key = ''
            )
        else:
            return ProjectBackupRepositoriesInner(
        )
        """

    def testProjectBackupRepositoriesInner(self):
        """Test ProjectBackupRepositoriesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
