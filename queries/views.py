from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.utils.timezone import now

from django.shortcuts import render, redirect
from queries.forms import QuestionForm,SolutionForm
from queries.models import QueryQuestion,QuerySolution
from services.models import Category, Tutorial
# Create your views here.


def queries(request):
    user = request.user
    categories = Category.objects.all()
    question = QueryQuestion.objects.filter(approval=True)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.pub_date = timezone.now()
            form.save()
            form = QuestionForm()

    context={
        'categories' :categories,
        'question' : question,
        'form': form
    }
    return render(request, 'queries/queries.html', context)

def filter(request,catego):
    user = request.user
    categories = Category.objects.all()
    question = QueryQuestion.objects.filter(approval=True,catego=catego)
    context={
        'categories' :categories,
        'question' : question
    }
    return render(request, 'queries/queries.html', context)

def solution(request,title):
    questio = QueryQuestion.objects.filter(title=title)
    for i in questio:
        a=i
    answer = QuerySolution.objects.filter(post=title)
    solform = SolutionForm()
    if request.method == 'POST':
        solform = SolutionForm(request.POST)
        if solform.is_valid():
            solform = solform.save(commit=False)
            solform.user = request.user
            solform.post = a
            solform.pub_date = timezone.now()
            solform.save()
            solform = SolutionForm()
            return redirect('queries')

    context={
        'questio' : questio,
        'solform' : solform,
        'answer': answer
    }
    return render(request, 'queries/solutions.html',context)

def search(request):
    categories = Category.objects.all()
    query = request.GET['query']
    print(query)
    if len(query) > 10 or len(query) < 1:
        question = []
    else:
        question = QueryQuestion.objects.filter(title__icontains=query)
    paras = {'question': question,
             'query': query,
             'categories' : categories}
    return render(request, 'queries/queries.html', paras)
