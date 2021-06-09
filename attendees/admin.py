from django.contrib import admin
from import_export import resources, admin as ie_admin

from . import models
from . import utils


class AttendeeResource(resources.ModelResource):

    class Meta:
        model = models.Attendee


class InvitationResource(resources.ModelResource):

    class Meta:
        model = models.Invitation


@admin.register(models.Attendee)
class AttendeeAdmin(ie_admin.ImportExportModelAdmin):
    list_display = utils.GetFieldsNameFromModel(models.Attendee)
    list_display_links =['mobile_phone',]
    resource_class = AttendeeResource


@admin.register(models.Invitation)
class InvitationAdmin(ie_admin.ImportExportModelAdmin):
    list_display = utils.GetFieldsNameFromModel(models.Invitation, add_id=True)
    resource_class = InvitationResource
