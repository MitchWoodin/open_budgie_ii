from open_budgie_ii.transaction_accounts.tests.factories import (
    TransactionAccountFactory,
)


class TestTransactionAccount:
    def test_factory(self):
        """
        A factory produces a valid transaction account.
        """

        transaction_account = TransactionAccountFactory()

        assert transaction_account.name != ""
        assert transaction_account.transaction_type != ""
        assert transaction_account.initial_balance == 0
        assert transaction_account.current_balance == 0
        assert transaction_account.net_worth == True
        assert transaction_account.user is not None
