from django.db import models
from django.urls import reverse

from . import utils


class Attendee(models.Model):
    civility = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True)


class Invitation(models.Model):
    attend_the_ceremony = models.BooleanField()
    attend_the_dinner = models.BooleanField()
    attend_the_party = models.BooleanField()
    sleep_at_domain = models.BooleanField()
    attend_the_brunch = models.BooleanField()
    is_eligible_to_sunday = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    hidden_comment = models.TextField(blank=True)
    attendees = models.ManyToManyField(Attendee, related_name="invitations")

    def get_hashid(self):
        return utils.h_encode(self.pk)

    def get_absolute_url(self):
        return reverse('attendees:invitation-update', kwargs={'pk': self.pk})
