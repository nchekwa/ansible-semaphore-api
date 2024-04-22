# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.models.schedule_request import ScheduleRequest

class TestScheduleRequest(unittest.TestCase):
    """ScheduleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduleRequest:
        """Test ScheduleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduleRequest`
        """
        model = ScheduleRequest()
        if include_optional:
            return ScheduleRequest(
                id = 56,
                cron_format = '* * * 1 *',
                project_id = 56,
                template_id = 56
            )
        else:
            return ScheduleRequest(
        )
        """

    def testScheduleRequest(self):
        """Test ScheduleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
