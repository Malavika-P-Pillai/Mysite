# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from polls.models import Question
from polls.models import Choice

# Create your views here.

"""def question_details(request,id):
    question = Question.objects.get(id = int(id))
    template = 'polls/question.html'
    context = {"question": question}
    return render(request, template, context)"""

class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/question.html'

class QuestionListView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'

def question_result(request,id):
    question = Question.objects.get(id=int(id))
    choices = Choice.objects.filter(question=question)
    template = 'polls/result.html'
    context = {"question": question,"choices":choices}
    return render(request, template, context)


def question_vote(request,id):
    question = Question.objects.get(id=int(id))
    if request.method == 'GET':
        choices = Choice.objects.filter(question=question)
        template = 'polls/vote.html'
        context = {"question": question, "choices": choices}
        return render(request, template, context)

    if request.method == "POST":
         id = int( request.POST['choice'])
         c = Choice.objects.get(id= id)
         c.votes += 1
         c.save()
         return redirect("view_result", question.id)





def index(request):
    question = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {"question": question}
    return render(request, template, context)
