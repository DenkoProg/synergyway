from celery import shared_task
import requests
from .models import User, Address, CreditCard

API_LIMIT = 1


@shared_task
def fetch_users():
    """
    Fetches a limited number of users from the placeholder API and updates or creates User records.
    """
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        response.raise_for_status()
        users_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch users: {e}")
        return

    for user_data in users_data[:API_LIMIT]:
        User.objects.update_or_create(
            external_id=user_data['id'],
            defaults={
                'name': user_data['name'],
                'username': user_data['username'],
                'email': user_data['email'],
                'phone': user_data['phone'],
                'website': user_data['website'],
            }
        )


@shared_task
def fetch_addresses():
    """
    Fetches random addresses for a limited number of users and updates or creates Address records.
    """
    users = User.objects.all()[:API_LIMIT]
    for user in users:
        try:
            response = requests.get('https://random-data-api.com/api/address/random_address')
            response.raise_for_status()

            address_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch address for user {user.id}: {e}")
            continue
        except ValueError:
            print(f"Invalid JSON response for user {user.id}")
            continue

        Address.objects.update_or_create(
            user_id=user,
            defaults={
                'street': address_data.get('street_name'),
                'suite': address_data.get('secondary_address', ''),
                'city': address_data.get('city'),
                'zipcode': address_data.get('zip_code'),
                'geo_lat': str(address_data.get('latitude', '')),
                'geo_lng': str(address_data.get('longitude', '')),
            }
        )


@shared_task
def fetch_credit_cards():
    """
    Fetches random credit card details for a limited number of users and updates or creates CreditCard records.
    """
    users = User.objects.all()[:API_LIMIT]
    for user in users:
        try:
            response = requests.get('https://random-data-api.com/api/business_credit_card/random_card')
            response.raise_for_status()

            cc_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch credit card for user {user.id}: {e}")
            continue
        except ValueError:
            print(f"Invalid JSON response for user {user.id}")
            continue

        CreditCard.objects.update_or_create(
            user_id=user,
            defaults={
                'cc_number': cc_data.get('credit_card_number'),
                'cc_type': cc_data.get('credit_card_type'),
                'expiration_date': cc_data.get('credit_card_expiry_date'),
            }
        )
