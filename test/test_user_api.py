# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from semaphore_api.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_user_get(self) -> None:
        """Test case for user_get

        Fetch logged in user
        """
        pass

    def test_user_tokens_api_token_id_delete(self) -> None:
        """Test case for user_tokens_api_token_id_delete

        Expires API token
        """
        pass

    def test_user_tokens_get(self) -> None:
        """Test case for user_tokens_get

        Fetch API tokens for user
        """
        pass

    def test_user_tokens_post(self) -> None:
        """Test case for user_tokens_post

        Create an API token
        """
        pass

    def test_users_get(self) -> None:
        """Test case for users_get

        Fetches all users
        """
        pass

    def test_users_post(self) -> None:
        """Test case for users_post

        Creates a user
        """
        pass

    def test_users_user_id_delete(self) -> None:
        """Test case for users_user_id_delete

        Deletes user
        """
        pass

    def test_users_user_id_get(self) -> None:
        """Test case for users_user_id_get

        Fetches a user profile
        """
        pass

    def test_users_user_id_password_post(self) -> None:
        """Test case for users_user_id_password_post

        Updates user password
        """
        pass

    def test_users_user_id_put(self) -> None:
        """Test case for users_user_id_put

        Updates user details
        """
        pass


if __name__ == '__main__':
    unittest.main()
