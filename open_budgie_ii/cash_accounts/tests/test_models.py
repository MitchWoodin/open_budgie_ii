from open_budgie_ii.cash_accounts.tests.factories import (
    CashAccountFactory,
)


class TestCashAccount:
    def test_cash_account_factory(self):
        """
        A factory produces a valid cash account.
        """

        cash_account = CashAccountFactory()

        assert cash_account.name != ""
        assert cash_account.initial_balance == 20
        assert cash_account.current_balance == 40
        assert cash_account.net_worth == True
        assert cash_account.user is not None
