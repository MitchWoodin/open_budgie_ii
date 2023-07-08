import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "accounts.User"

    username = factory.Sequence(lambda n: "user{0}".format(n))
    email = factory.Sequence(lambda n: "user{0}@example.com".format(n))
    password = factory.PostGenerationMethodCall("set_password", "password")
    is_active = True

