from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from django.utils.timezone import now
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, redirect
from services.forms import ContactUsForm, PurchaseForm, TutorialForm,UserprofileForm
from services.models import Category, Tutorial, Purchase, Userprofile
from queries.models import QueryQuestion
# Create your views here.


def index(request):
    categories = Category.objects.all()
    context={
        'categories':categories
        }
    return render(request, 'services/index.html',context)

def alltutorials(request):
    categories = Category.objects.all() 
    tutorial = Tutorial.objects.filter(approval=True).order_by('-timestamp')
    context={
        'categories' :categories,
        'tutorial' : tutorial
    }
    return render(request, 'services/alltutorials.html',context)

def tfilter(request,catego):
    user = request.user
    categories = Category.objects.all()
    tutorial = Tutorial.objects.filter(approval=True,catego=catego)
    context={
        'categories' :categories,
        'tutorial' : tutorial
    }
    return render(request, 'services/alltutorials.html', context)

def tutorial_details(request,title):
    user = request.user
    categories = Category.objects.all() 
    details = Tutorial.objects.filter(title=title)

    popular = Tutorial.objects.all()[0:4]
    tutori= Tutorial.objects.filter(title=title)
    for i in tutori:
        a=i
    if user.is_authenticated:
        purchase = Purchase.objects.filter(customuser=request.user).values('tuto')
        res = [sub['tuto'] for sub in purchase]
        form = PurchaseForm()
        if request.method == 'POST':
            form = PurchaseForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.customuser = user
                form.tuto = a
                form.purchasedate = timezone.now()
                form.save()
                form = PurchaseForm()
                return redirect('mycourse')
        context = {
                'details': details,
                'form': form,
                'res':res,
                'popular': popular
                }
        return render(request, 'services/tutorial_details.html',context)
    else:
        context = {
                'details': details,
                'popular': popular
            }
        print(context)
        return render(request, 'services/tutorial_details.html', context)

@login_required
def mycourse(request):
    user = request.user
    if request.user.is_authenticated:
        mycourse = Purchase.objects.filter(customuser=request.user).values('tuto')
        res = [ sub['tuto'] for sub in mycourse ]
        delete = Tutorial.objects.filter(title__in=res)
        context={
                'delete':delete,
                }
        return render(request,'services/mycourse.html', context)

@login_required
def tutorial(request,title):
    if request.user.is_authenticated:
        course = Tutorial.objects.filter(title=title)
        return render(request,'services/tutorials.html',{'course':course})


@login_required
def addtutorial(request):
    profile = Userprofile.objects.filter(email=request.user.email)
    form = TutorialForm()
    if request.method == 'POST':
        form = TutorialForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.timestamp = timezone.now()
            form.save()
            form = TutorialForm()
            return redirect('alltutorials')
    context = {'form': form,
                'profile' : profile 
            }
    return render(request,'services/addtutorial.html',context)

def contact(request):
    form = ContactUsForm()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactUsForm()
    context = {'form': form}
    return render(request, 'services/contact.html', context)


@login_required
def profilee(request):
    user = request.user
    if user.is_authenticated:
        deletequery = QueryQuestion.objects.filter(approval=False)
        deleteser = Tutorial.objects.filter(approval=False)
        if len(deletequery)>0:
            for i in deletequery:
                deletedquery=i
                messages.success(request,deletedquery)
            deletequery.delete()
            return redirect('profilee')

        elif len(deleteser)>0:
            for e in deleteser:
                deletedser=i
                messages.success(request,deletedser)
            deleteser.delete()
            return redirect('profilee')
        else:
            profile = Userprofile.objects.filter(email=request.user.email)
            userquery = QueryQuestion.objects.filter(author=user)
            userser = Tutorial.objects.filter(author=user)
            userform = UserprofileForm()
            if request.method == 'POST':
                userform = UserprofileForm(request.POST,request.FILES)
                if userform.is_valid():
                    userform = userform.save(commit=False)
                    userform.firstname = request.user.first_name
                    userform.lastname = request.user.last_name
                    userform.email = request.user.email
                    userform.save()
                    userform = UserprofileForm()
                    return redirect('profilee')
            context={
                'userquery': userquery,
                'userser': userser,
                'user':user,
                'userform': userform,
                'profile': profile
                }    
            return render(request, 'queries/profilequeri.html', context)
    else:
        return redirect('account_login')


def delete_querie(request,title):
    user = request.user
    if user.is_authenticated:
        deletequery = QueryQuestion.objects.filter(title=title)
        deletetutorial = Tutorial.objects.filter(title=title)
        deletequery.delete()
        deletetutorial.delete()
        return redirect('profilee')
