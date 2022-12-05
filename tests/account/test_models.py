import pytest
from account.models import Account
from tests.account.factories import AccountFactory


@pytest.mark.django_db
def test_user__str__():
    instance = AccountFactory()
    assert instance.id
    assert instance.email
    assert instance.first_name
    assert isinstance(instance, Account)
