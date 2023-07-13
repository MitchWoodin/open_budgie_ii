from open_budgie_ii.transactions.tests.factories import TransactionFactory


class TestTransaction:
    def test_factory(self):
        """
        A transaction factory produces a valid transaction:
        """

        transaction = TransactionFactory()

        assert transaction.date is not None
        assert transaction.description != ""
