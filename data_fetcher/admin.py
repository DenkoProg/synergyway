from django.contrib import admin
from .models import User, Address, CreditCard

admin.site.register(User)
admin.site.register(Address)
admin.site.register(CreditCard)
