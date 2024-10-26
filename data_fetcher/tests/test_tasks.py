import pytest
from ..models import User, Address, CreditCard
from ..tasks import fetch_users, fetch_addresses, fetch_credit_cards

@pytest.mark.django_db
def test_fetch_users_creates_users():
    fetch_users()
    users_count = User.objects.count()
    assert users_count > 0, f"Expected at least 1 user, found {users_count}"


@pytest.mark.django_db
def test_fetch_addresses_creates_addresses():
    fetch_users()
    fetch_addresses()
    addresses_count = Address.objects.count()
    users_count = User.objects.count()
    assert addresses_count == users_count, (
        f"Expected {users_count} addresses, found {addresses_count}"
    )


@pytest.mark.django_db
def test_fetch_credit_cards_creates_credit_cards():
    fetch_users()
    fetch_credit_cards()
    credit_cards_count = CreditCard.objects.count()
    users_count = User.objects.count()
    assert credit_cards_count == users_count, (
        f"Expected {users_count} credit cards, found {credit_cards_count}"
    )
