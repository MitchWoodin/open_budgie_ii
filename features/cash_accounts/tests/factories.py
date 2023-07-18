import factory

from features.user_accounts.tests.factories import UserFactory


class CashAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "cash_accounts.CashAccount"

    name = factory.Sequence(lambda n: f"user_{n}")
    initial_balance = 20
    current_balance = initial_balance + 20
    net_worth = True

    user = factory.SubFactory("features.user_accounts.tests.factories.UserFactory")
