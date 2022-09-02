from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from .forms import QuestionForm
from .models import Question, Contactus, Category
from django.contrib.auth import authenticate, get_user_model, login, logout
from base.models import Client, Question, Technology, Assignment, Interviewee
from users.forms import IntervieweeForm


def AddQuestion(request):
    form = QuestionForm()
    client = request.session['client']
    category = request.session['category_name']
    #question_python = Question.objects.filter(client__name=client).filter(technology__technology_name="Python").filter(category__category_name=category)
    #question_python_count = len(question_python)
    #question_django = Question.objects.filter(client__name=client).filter(technology__technology_name="Django").filter(category__category_name=category)
    #question_django_count = len(question_django)
    if request.method == 'POST':
        q = request.POST.get('question')
        print(q)
        form = QuestionForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('question')
    return render(request, 'base/addquestion.html', {'form': form})


def ViewQuestion(request):
    client = request.session['client']
    category = request.session['category_name']
    question_python = Question.objects.filter(client__name=client).filter(technology__technology_name="Python").filter(
        category__category_name=category)
    question_python_count = len(question_python)
    question_docker = Question.objects.filter(client__name=client).filter(technology__technology_name="Docker").filter(
        category__category_name=category)
    question_docker_count = len(question_docker)
    question_sql = Question.objects.filter(client__name=client).filter(technology__technology_name="SQL").filter(
        category__category_name=category)
    question_sql_count = len(question_sql)
    question_django = Question.objects.filter(client__name=client).filter(technology__technology_name="Django").filter(
        category__category_name=category)
    question_django_count = len(question_django)
    user = request.user
    result = Assignment.objects.all().filter(user__email=user)

    return render(request, 'base/show.html',
                  {'question_python': question_python, 'question_django': question_django,
                   'client':client, 'category':category, 'question_python_count':question_python_count,
                   'question_django_count': question_django_count, 'question_docker':question_docker,'question_docker_count':question_docker_count,'question_sql':question_sql,'question_sql_count':question_sql_count,'result':result})


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contactus(name=name, email=email, message=message)
        contact.save()
        return redirect('/user')
    return render(request, 'users/contactus.html')


def ViewResult(request):
    user = request.user
    client = request.session['client']
    print(client)
    result = Assignment.objects.filter(user__email=user).filter(client__name=client)
    count_result = len(result)
    print(count_result)
    return render(request, 'users/result.html', {'result': result, 'count_result': count_result, 'client':client})


def AssignView(request):
    form1 = IntervieweeForm()
    if request.method == 'POST':
        form1 = IntervieweeForm(request.POST)
        if form1.is_valid():
            user = form1.save(commit=False)
            user.user = request.user
            user.save()
            client = form1.cleaned_data['client']
            request.session['client'] = str(client)
            category = form1.cleaned_data['category_name']
            request.session['category_name'] = str(category)
            print(request.session['category_name'])
            return redirect('viewquestion')
    try:
        user = request.session['user']
    except KeyError:
        return redirect('login')

    user1 = Assignment.objects.all().filter(user__email=user)
    if user in Assignment.objects.filter(user__email=user):
        user1 = user
    return render(request, 'users/dashboard.html', {'user1': user1, 'form1': form1})


