from django.views.generic.edit import UpdateView, FormView

from . import models
from . import utils
from . import forms
import attendees


class InvitationUpdateView(UpdateView):
    model = models.Invitation
    fields = utils.GetFieldsNameFromModel(model)


class InvitationReplyView(FormView):
    template_name = 'attendees/reply.html'
    form_class = forms.InvitationReplyForm

    def form_valid(self, form):
        mobile_phone = form.cleaned_data['mobile_phone']
        attendee = models.Attendee.objects.get(mobile_phone=mobile_phone)
        invitations = models.Invitation.objects.filter(attendees__in=[attendee,])
        invitation = invitations[0]
        self.success_url = invitation.get_absolute_url()
        return super().form_valid(form)
