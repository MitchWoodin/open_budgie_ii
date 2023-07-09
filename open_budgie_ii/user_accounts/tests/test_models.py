import pytest

from open_budgie_ii.user_accounts.tests.factories import UserFactory


class TestUser:
    def test_create_user(self):
        """
        Test that an unauthenticated user gets a valid response.
        """

        user = UserFactory()

        assert user is not None
