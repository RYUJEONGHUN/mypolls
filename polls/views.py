from django.http import HttpResponse
from django.template import loader
from .models import Choice, Question
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
  latest_question_list=Question.objects.order_by('-pub_date')[:5]
  #template=loader.get_template('polls/index.html')
  context={
    'latest_question_list': latest_question_list,
  }
  return render(request, 'polls/index.html', context)

def detail(request, question_id):
  #try:
  # question=get_object_or_404(Question,pk=question_id)
  #except Question.DoesNotExist:
  # raise Http404("Question does not exist")
  question=get_object_or_404(Question,pk=question_id)
  return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
  question=get_object_or_404(Question,pk=question_id)
  return render(request,'polls/results.html',{'question':question})  

def vote(request, question_id):
  question=get_object_or_404(Question, pk=question_id)
  try:
    selected_choice=question.choice_set.get(pk=request.POST['choice'])
  except(KeyError,choice.DoesNotException):
    return render(request,'polls/detail.html',{
      'question':question,
      'error_message':"You didn't select a choice.",
    })
  else:
    selected_choice.votes+=1
    selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
# Create your views here.
