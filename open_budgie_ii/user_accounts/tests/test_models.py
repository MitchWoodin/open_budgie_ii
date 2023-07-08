from openbudgie_ii.user_accounts.tests.factories import UserFactory


class TestUser:
    def test_create_user(self):
        user = UserFactory()

        assert user is not None
