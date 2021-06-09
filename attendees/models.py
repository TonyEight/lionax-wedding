from django.db import models


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
