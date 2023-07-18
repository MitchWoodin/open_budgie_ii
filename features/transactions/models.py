from django.db import models


class Transaction(models.Model):
    """
    Model logs users transactions and spendings.
    """

    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100)
    source_account = models.OneToOneField(
        "cash_accounts.CashAccount",
        on_delete=models.CASCADE,
    )
    destination_account = models.CharField(max_length=100)
    amount = models.FloatField()
    budget = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    recurring = models.BooleanField(default=False)
