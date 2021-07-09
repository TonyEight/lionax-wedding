from django.urls import path

from . import views


app_name = "frontpage"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("information", views.InformationView.as_view(), name="information"),
    path("wedding-list", views.WeddingListView.as_view(), name="wedding-list"),
]
