import pytest
from rest_framework.exceptions import ValidationError

from profiles.models import Profiles, Article, validate_profile_age
from tests.profiles.factories import ArticleFactory, ProfileFactory


@pytest.mark.django_db
def test_profiles_models():
    profile = ProfileFactory()
    assert profile.name
    assert profile.email
    assert profile.age
    assert isinstance(profile, Profiles)


@pytest.mark.django_db
def test_Article_models():
    article = ArticleFactory()
    assert article.title
    assert article.profile
    assert isinstance(article, Article)


@pytest.mark.django_db
def test_age_is_valid():
    with pytest.raises(ValidationError, match="you don't have the access "):
        validate_profile_age(18)
