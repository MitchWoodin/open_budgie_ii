from django.db import models


class TransactionAccount(models.Model):
    """
    An account for transactions to be made.
    """

    name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    initial_balance = models.FloatField()
    current_balance = models.FloatField()
    net_worth = models.BooleanField()
    user = models.OneToOneField(
        "user_accounts.User",
        on_delete=models.CASCADE,
    )
