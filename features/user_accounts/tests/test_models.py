import pytest

from features.user_accounts.tests.factories import UserFactory


class TestUser:
    def test_create_user(self):
        """
        Test that an unauthenticated user gets a valid response.
        """

        user = UserFactory()

        assert user is not None
