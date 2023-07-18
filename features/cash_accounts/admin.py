from django.contrib import admin

from .models import CashAccount


@admin.register(CashAccount)
class CashAccountAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "current_balance"]
    raw_id_fields = ["user"]
