# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.api.project_api import ProjectApi


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectApi()

    def tearDown(self) -> None:
        pass

    def test_project_project_id_delete(self) -> None:
        """Test case for project_project_id_delete

        Delete project
        """
        pass

    def test_project_project_id_environment_environment_id_delete(self) -> None:
        """Test case for project_project_id_environment_environment_id_delete

        Removes environment
        """
        pass

    def test_project_project_id_environment_environment_id_put(self) -> None:
        """Test case for project_project_id_environment_environment_id_put

        Update environment
        """
        pass

    def test_project_project_id_environment_get(self) -> None:
        """Test case for project_project_id_environment_get

        Get environment
        """
        pass

    def test_project_project_id_environment_post(self) -> None:
        """Test case for project_project_id_environment_post

        Add environment
        """
        pass

    def test_project_project_id_events_get(self) -> None:
        """Test case for project_project_id_events_get

        Get Events related to this project
        """
        pass

    def test_project_project_id_get(self) -> None:
        """Test case for project_project_id_get

        Fetch project
        """
        pass

    def test_project_project_id_inventory_get(self) -> None:
        """Test case for project_project_id_inventory_get

        Get inventory
        """
        pass

    def test_project_project_id_inventory_inventory_id_delete(self) -> None:
        """Test case for project_project_id_inventory_inventory_id_delete

        Removes inventory
        """
        pass

    def test_project_project_id_inventory_inventory_id_put(self) -> None:
        """Test case for project_project_id_inventory_inventory_id_put

        Updates inventory
        """
        pass

    def test_project_project_id_inventory_post(self) -> None:
        """Test case for project_project_id_inventory_post

        create inventory
        """
        pass

    def test_project_project_id_keys_get(self) -> None:
        """Test case for project_project_id_keys_get

        Get access keys linked to project
        """
        pass

    def test_project_project_id_keys_key_id_delete(self) -> None:
        """Test case for project_project_id_keys_key_id_delete

        Removes access key
        """
        pass

    def test_project_project_id_keys_key_id_put(self) -> None:
        """Test case for project_project_id_keys_key_id_put

        Updates access key
        """
        pass

    def test_project_project_id_keys_post(self) -> None:
        """Test case for project_project_id_keys_post

        Add access key
        """
        pass

    def test_project_project_id_put(self) -> None:
        """Test case for project_project_id_put

        Update project
        """
        pass

    def test_project_project_id_repositories_get(self) -> None:
        """Test case for project_project_id_repositories_get

        Get repositories
        """
        pass

    def test_project_project_id_repositories_post(self) -> None:
        """Test case for project_project_id_repositories_post

        Add repository
        """
        pass

    def test_project_project_id_repositories_repository_id_delete(self) -> None:
        """Test case for project_project_id_repositories_repository_id_delete

        Removes repository
        """
        pass

    def test_project_project_id_repositories_repository_id_put(self) -> None:
        """Test case for project_project_id_repositories_repository_id_put

        Updates repository
        """
        pass

    def test_project_project_id_role_get(self) -> None:
        """Test case for project_project_id_role_get

        Fetch permissions of the current user for project
        """
        pass

    def test_project_project_id_tasks_get(self) -> None:
        """Test case for project_project_id_tasks_get

        Get Tasks related to current project
        """
        pass

    def test_project_project_id_tasks_last_get(self) -> None:
        """Test case for project_project_id_tasks_last_get

        Get last 200 Tasks related to current project
        """
        pass

    def test_project_project_id_tasks_post(self) -> None:
        """Test case for project_project_id_tasks_post

        Starts a job
        """
        pass

    def test_project_project_id_tasks_task_id_delete(self) -> None:
        """Test case for project_project_id_tasks_task_id_delete

        Deletes task (including output)
        """
        pass

    def test_project_project_id_tasks_task_id_get(self) -> None:
        """Test case for project_project_id_tasks_task_id_get

        Get a single task
        """
        pass

    def test_project_project_id_tasks_task_id_output_get(self) -> None:
        """Test case for project_project_id_tasks_task_id_output_get

        Get task output
        """
        pass

    def test_project_project_id_tasks_task_id_stop_post(self) -> None:
        """Test case for project_project_id_tasks_task_id_stop_post

        Stop a job
        """
        pass

    def test_project_project_id_templates_get(self) -> None:
        """Test case for project_project_id_templates_get

        Get template
        """
        pass

    def test_project_project_id_templates_post(self) -> None:
        """Test case for project_project_id_templates_post

        create template
        """
        pass

    def test_project_project_id_templates_template_id_delete(self) -> None:
        """Test case for project_project_id_templates_template_id_delete

        Removes template
        """
        pass

    def test_project_project_id_templates_template_id_get(self) -> None:
        """Test case for project_project_id_templates_template_id_get

        Get template
        """
        pass

    def test_project_project_id_templates_template_id_put(self) -> None:
        """Test case for project_project_id_templates_template_id_put

        Updates template
        """
        pass

    def test_project_project_id_users_get(self) -> None:
        """Test case for project_project_id_users_get

        Get users linked to project
        """
        pass

    def test_project_project_id_users_post(self) -> None:
        """Test case for project_project_id_users_post

        Link user to project
        """
        pass

    def test_project_project_id_users_user_id_delete(self) -> None:
        """Test case for project_project_id_users_user_id_delete

        Removes user from project
        """
        pass

    def test_project_project_id_views_get(self) -> None:
        """Test case for project_project_id_views_get

        Get view
        """
        pass

    def test_project_project_id_views_post(self) -> None:
        """Test case for project_project_id_views_post

        create view
        """
        pass

    def test_project_project_id_views_view_id_delete(self) -> None:
        """Test case for project_project_id_views_view_id_delete

        Removes view
        """
        pass

    def test_project_project_id_views_view_id_get(self) -> None:
        """Test case for project_project_id_views_view_id_get

        Get view
        """
        pass

    def test_project_project_id_views_view_id_put(self) -> None:
        """Test case for project_project_id_views_view_id_put

        Updates view
        """
        pass


if __name__ == '__main__':
    unittest.main()
