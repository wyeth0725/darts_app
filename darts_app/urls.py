from django.urls import path

from . import views


app_name = "darts_app"
urlpatterns = [
    path("", views.index, name="index"),
]