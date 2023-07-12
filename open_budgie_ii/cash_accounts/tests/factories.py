import factory

from open_budgie_ii.user_accounts.tests.factories import UserFactory


class CashAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "cash_accounts.CashAccount"

    name = factory.Sequence(lambda n: f"user_{n}")
    transaction_type = factory.Sequence(lambda n: f"type_{n}")
    initial_balance = 20
    current_balance = initial_balance + 20
    net_worth = True

    user = factory.SubFactory(
        "open_budgie_ii.user_accounts.tests.factories.UserFactory"
    )