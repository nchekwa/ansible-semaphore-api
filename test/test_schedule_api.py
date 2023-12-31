# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.api.schedule_api import ScheduleApi


class TestScheduleApi(unittest.TestCase):
    """ScheduleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ScheduleApi()

    def tearDown(self) -> None:
        pass

    def test_project_project_id_schedules_post(self) -> None:
        """Test case for project_project_id_schedules_post

        create schedule
        """
        pass

    def test_project_project_id_schedules_schedule_id_delete(self) -> None:
        """Test case for project_project_id_schedules_schedule_id_delete

        Deletes schedule
        """
        pass

    def test_project_project_id_schedules_schedule_id_get(self) -> None:
        """Test case for project_project_id_schedules_schedule_id_get

        Get schedule
        """
        pass

    def test_project_project_id_schedules_schedule_id_put(self) -> None:
        """Test case for project_project_id_schedules_schedule_id_put

        Updates schedule
        """
        pass


if __name__ == '__main__':
    unittest.main()
