from django.contrib import admin
from django.urls import include, path

from open_budgie_ii.core.views import index

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("allauth.urls")),
    path("firm-office/", admin.site.urls),
]
