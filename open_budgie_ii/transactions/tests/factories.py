import datetime

import factory


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "transactions.Transaction"

    date = factory.LazyFunction(datetime.datetime.now)
    description = factory.Faker("word")
    source_account = factory.SubFactory(
        "open_budgie_ii.cash_accounts.tests.factories.CashAccountFactory"
    )
    destination_account = factory.Faker("word")
    amount = 23.32
    budget = factory.Faker("word")
    category = factory.Faker("word")
