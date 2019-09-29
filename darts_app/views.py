import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import User
from .forms import register_form

def index(request):
    try:
        user_list = User.objects.all().order_by("-register_date")[:5]
        context = {"user_list": user_list}
        return render(request, "darts_app/index.html", context)
    except Exception:
        error_message = "error"

def register_user(request):
    try:
        context = {
            "form": register_form(),
            "error_message": ""
        }
        if (request.method == "POST"):
            context["user_name"] = request.POST["user_name"]
        return render(request, "darts_app/register_user.html", context)
    except Exception:
        error_message = "error"

def register_result(request):
    try:
        new_user = request.POST["user_name"]
        existing_user = list(User.objects.values("user_name"))
        context = {"error_message": ""}
        if {"user_name": new_user} in existing_user:
            context["error_message"] = "register failed."
            context["error_message"] += "duplicate name."
            return render(request, "darts_app/register_result.html", context)
        new_rec = User(user_name=new_user, register_date=datetime.datetime.now())
        new_rec.save()
        return render(request, "darts_app/register_result.html", context)
    except Exception:
        error_message = "error"