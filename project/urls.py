from django.contrib import admin
from django.urls import include, path

from features.core.views import index

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("allauth.urls")),
    path("firm-office/", admin.site.urls),
]
