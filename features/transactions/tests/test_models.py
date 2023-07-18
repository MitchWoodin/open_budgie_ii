from features.transactions.tests.factories import TransactionFactory


class TestTransaction:
    def test_transaction_factory(self):
        """
        A transaction factory produces a valid transaction:
        """

        transaction = TransactionFactory()

        assert transaction.date is not None
        assert transaction.description != ""
