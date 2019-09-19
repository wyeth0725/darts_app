from django.shortcuts import render

from .models import Question

def index(request):
    #order by の引数の前に-つけるとdescになる
    latest_question_list = Question.objects.all().order_by("-publish_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "darts_app/index.html", context)