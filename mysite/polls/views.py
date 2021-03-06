from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/details.html', context)

def results(request, question_id):
    return HttpResponse(f'Esses são os resultados da pergunta de número {question_id}')

def vote(request, question_id):
    return HttpResponse(f'Você está votando na pergunta de número {question_id}')