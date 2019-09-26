from django.urls import path

from . import views


app_name = "darts_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("darts_app/register_user", views.register_user, name="register_user"),
    path("darts_app/register_result", views.register_result, name="register_result"),
]