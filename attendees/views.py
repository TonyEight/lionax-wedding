from django.views.generic.edit import UpdateView, FormView

from . import models
from . import utils
from . import forms


class InvitationUpdateView(UpdateView):
    model = models.Invitation
    fields = utils.GetFieldsNameFromModel(model)


class InvitationReplyView(FormView):
    template_name = 'attendees/reply.html'
    form_class = forms.InvitationReplyFormm

    def form_valid(self, form):
        self.success_url = self.form.retrieve_invitation()
        return super().form_valid(form)
