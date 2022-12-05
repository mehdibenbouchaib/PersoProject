import factory
from factory import Faker

from profiles.models import Profiles, Article


class ProfileFactory(factory.django.DjangoModelFactory):
    name = Faker("name")
    email = Faker("email")

    class Meta:
        model = Profiles


class ArticleFactory(factory.django.DjangoModelFactory):
    title = Faker("text")
    profile = factory.SubFactory(ProfileFactory)

    class Meta:
        model = Article
