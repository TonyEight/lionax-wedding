from django.urls import path, register_converter

from . import views
from . import utils

register_converter(utils.HashIdConverter, "hashid")

app_name = "attendees"
urlpatterns = [
    path('invitation/<hashid:pk>/', views.InvitationUpdateView.as_view(),
         name='invitation-update'),
    path('invitation/reply/', views.InvitationReplyView.as_view(),
         name='invitation-reply'),
]
