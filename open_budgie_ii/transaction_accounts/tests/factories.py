import factory

from open_budgie_ii.user_accounts.tests.factories import UserFactory


class TransactionAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "transaction_accounts.TransactionAccount"

    name = factory.Sequence(lambda n: f"user_{n}")
    initial_balance = 20
    current_balance = initial_balance + 20
    user = UserFactory()
