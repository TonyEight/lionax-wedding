# Generated by Django 3.1.6 on 2021-07-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendees', '0004_invitation_last_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
