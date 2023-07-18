import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "user_accounts.User"

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_active = True
