from django.db import models


class TransactionAccount(models.Model):
    """
    An account for transactions to be made.
    """

    name = models.CharField(max_length=100)
