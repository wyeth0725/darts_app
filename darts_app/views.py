from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import User


def index(request):
    user_list = User.objects.all().order_by("-register_date")[:5]
    context = {"user_list": user_list}
    return render(request, "darts_app/index.html", context)

def register_user(request):
    if request.method == "POST":
        f = register_result(request.POST)
    else:
        f = register_result()
    context = {"user_name", f}
    return render(request, "darts_app/register_user.html", context)

def register_result(request, user_name):

    return render(request, "darts_app/register_result.html")

"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "darts_app/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "darts_app/detail.html", {"question": question, "error_message": "You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("darts_app:results", args=(question.id)))
"""