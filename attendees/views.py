from django.db import reset_queries
from django.http import response
from django.views.generic.edit import UpdateView, FormView
from easyaudit import models as easyaudit_models

from . import models
from . import utils
from . import forms


class InvitationUpdateView(UpdateView):
    model = models.Invitation
    fields = utils.GetFieldsNameFromModel(model)

    def form_valid(self, form):
        last_editor_hashid = self.request.GET.get('lid')
        if last_editor_hashid:
            self.success_url = self.get_success_url() + '?lid={0}'.format(last_editor_hashid)
        else:
            attendee = self.object.attendees.filter(first_name=form.cleaned_data['last_editor'])[0]
            self.success_url = self.get_success_url() + '?lid={0}'.format(utils.h_encode(attendee.id))
        form.instance.accept_to_pay = form.instance.sleep_at_domain
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_editor_hashid = self.request.GET.get('lid')
        if last_editor_hashid:
            last_editor = models.Attendee.objects.get(id=utils.h_decode(last_editor_hashid))
            context['last_editor'] = last_editor.first_name
        from django.contrib.contenttypes.models import ContentType
        events = easyaudit_models.CRUDEvent.objects.filter(
            content_type=ContentType.objects.get_for_model(model=self.model),
            object_id=self.object.id
        ).order_by('-datetime')
        if events:
            context['last_change'] = events[0]
        return context


class InvitationReplyView(FormView):
    template_name = 'attendees/reply.html'
    form_class = forms.InvitationReplyForm

    def form_valid(self, form):
        mobile_phone = form.cleaned_data['mobile_phone']
        try:
            attendee = models.Attendee.objects.get(mobile_phone=mobile_phone)
        except models.Attendee.DoesNotExist:
            return self.form_invalid(form)
        invitations = models.Invitation.objects.filter(attendees__in=[attendee,])
        invitation = invitations[0]
        self.success_url = invitation.get_absolute_url()
        self.success_url += '?lid={0}'.format(utils.h_encode(attendee.id))
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form, 
                error_message="number_not_found"
            )
        )
