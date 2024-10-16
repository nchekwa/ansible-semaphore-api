# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.project_backup import ProjectBackup

class TestProjectBackup(unittest.TestCase):
    """ProjectBackup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBackup:
        """Test ProjectBackup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBackup`
        """
        model = ProjectBackup()
        if include_optional:
            return ProjectBackup(
                meta = semaphore_api.models.project_backup_meta.ProjectBackup_meta(
                    name = '', 
                    alert = True, 
                    max_parallel_tasks = 0, ),
                templates = [
                    semaphore_api.models.project_backup_templates_inner.ProjectBackup_templates_inner(
                        inventory = '', 
                        repository = '', 
                        environment = '', 
                        view = '', 
                        name = '', 
                        playbook = '', 
                        description = '', 
                        allow_override_args_in_task = True, 
                        suppress_success_alerts = True, 
                        autorun = True, 
                        type = '', )
                    ],
                repositories = [
                    semaphore_api.models.project_backup_repositories_inner.ProjectBackup_repositories_inner(
                        name = '', 
                        git_url = '', 
                        git_branch = '', 
                        ssh_key = '', )
                    ],
                keys = [
                    semaphore_api.models.project_backup_keys_inner.ProjectBackup_keys_inner(
                        name = '', 
                        type = 'ssh', )
                    ],
                views = [
                    semaphore_api.models.project_backup_views_inner.ProjectBackup_views_inner(
                        name = '', 
                        position = 0, )
                    ],
                inventories = [
                    semaphore_api.models.project_backup_inventories_inner.ProjectBackup_inventories_inner(
                        name = '', 
                        inventory = '', 
                        type = 'static', )
                    ],
                environments = [
                    semaphore_api.models.project_backup_environments_inner.ProjectBackup_environments_inner(
                        name = '', 
                        json = '', )
                    ]
            )
        else:
            return ProjectBackup(
        )
        """

    def testProjectBackup(self):
        """Test ProjectBackup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()