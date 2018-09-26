from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib.parse as urlparse
import json
from .models import Question
from datetime import datetime

@csrf_exempt
def index(request):
    questions = Question.objects.all()
    str = ''
    for question in questions:
        str += "Status : '{}' - Time : {}<br>".format(question.question_text, question.now1)
    return HttpResponse(str)

@csrf_exempt
def save(request):
    questions = Question.objects.all()
    if request.method == "PUT" :
        http_s = "http://django/django?" + request.read().decode('utf-8')
        p = urlparse.urlparse(http_s)
        question_text = urlparse.parse_qs(p.query)['question_text'][0]
        now1 = datetime.today().strftime("%Y/%m/%d/%H:%M")
        question =  Question(question_text = question_text, now1 = now1)
        question.save()
    return HttpResponse("data received")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
