from django.urls import path

from . import views


app_name = "frontpage"
urlpatterns = [
    path("", views.FrontPageGenericView.as_view(), name="index"),
    path("information", views.FrontPageGenericView.as_view(), name="information"),
    path("wedding-list", views.FrontPageGenericView.as_view(), name="wedding-list"),
]
