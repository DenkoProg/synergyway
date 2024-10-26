import uuid
from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    geo_lat = models.CharField(max_length=50)
    geo_lng = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}"


class CreditCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='credit_card')
    cc_number = models.CharField(max_length=20)
    cc_type = models.CharField(max_length=50)
    expiration_date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.cc_type} ending with {self.cc_number[-4:]}"
