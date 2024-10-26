# Generated by Django 5.1.2 on 2024-10-26 08:50

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('external_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cc_number', models.CharField(max_length=20)),
                ('cc_type', models.CharField(max_length=50)),
                ('expiration_date', models.CharField(max_length=10)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='credit_card', to='data_fetcher.user')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=255)),
                ('suite', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('geo_lat', models.CharField(max_length=50)),
                ('geo_lng', models.CharField(max_length=50)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                                 related_name='address', to='data_fetcher.user')),
            ],
        ),
    ]