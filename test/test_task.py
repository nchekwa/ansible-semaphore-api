# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.task import Task

class TestTask(unittest.TestCase):
    """Task unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Task:
        """Test Task
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Task`
        """
        model = Task()
        if include_optional:
            return Task(
                id = 23,
                template_id = 56,
                status = '',
                debug = True,
                playbook = '',
                environment = '',
                secret = '',
                limit = ''
            )
        else:
            return Task(
        )
        """

    def testTask(self):
        """Test Task"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
