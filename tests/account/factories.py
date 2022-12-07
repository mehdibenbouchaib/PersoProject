import factory.django
from factory import Faker

from account.models import Account


class AccountFactory(factory.django.DjangoModelFactory):
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")

    class Meta:
        model = Account

    class Params:
        superuser = factory.Trait(is_staff=True, is_superuser=True)
        staff = factory.Trait(is_staff=True)
