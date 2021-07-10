from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from . import utils


class Attendee(models.Model):
    civility = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_phone = PhoneNumberField(unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.civility, self.first_name, self.last_name)


class Invitation(models.Model):
    attend_the_ceremony = models.BooleanField()
    attend_the_dinner = models.BooleanField()
    attend_the_party = models.BooleanField()
    sleep_at_domain = models.BooleanField(default=False)
    accept_to_pay = models.BooleanField(default=False)
    attend_the_brunch = models.BooleanField(default=False)
    is_eligible_to_sunday = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    hidden_comment = models.TextField(blank=True)
    last_editor = models.CharField(max_length=255, default="Axelle et Ludovic", blank=True)
    attendees = models.ManyToManyField(Attendee, related_name="invitations")

    def _get_first_attendee(self):
        return self.attendees.all()[0]

    def get_hashid(self):
        return utils.h_encode(self.pk)

    def __str__(self):
        return 'Invitation {0} ({1})'.format(self.pk, self._get_first_attendee().last_name)

    def get_absolute_url(self):
        return reverse('attendees:invitation-update', kwargs={'pk': self.pk})
