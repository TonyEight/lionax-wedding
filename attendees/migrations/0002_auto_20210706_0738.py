# Generated by Django 3.1.6 on 2021-07-06 07:38

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
