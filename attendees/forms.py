from django import forms
from django.db.models.base import ModelBase
from phonenumber_field.formfields import PhoneNumberField

from . import models


class InvitationReplyForm(forms.Form):
    mobile_phone = PhoneNumberField(required=True, widget=forms.widgets.TextInput(
        attrs={"placeholder": "Saisissez votre numéro"}))
