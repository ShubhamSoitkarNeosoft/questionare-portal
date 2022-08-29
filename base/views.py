from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from .forms import QuestionForm
from .models import Question, Contactus
from django.contrib.auth import authenticate, get_user_model, login, logout
from base.models import Client, Question, Technology


def AddQuestion(request):
    form = QuestionForm()
    client = request.session['client']
    category = request.session['category_name']
    question_python = Question.objects.filter(client__name=client).filter(technology__technology_name="python").filter(category__category_name=category)
    question_django = Question.objects.filter(client__name=client).filter(technology__technology_name="django").filter(category__category_name=category)
    if request.method == 'POST':
        form1 = QuestionForm(request.POST)
        if form1.is_valid():
            form1.save()
        return redirect('question')
    return render(request, 'base/question.html', {'form': form,'question_python': question_python, 'question_django': question_django, 'client':client, 'category': category})


def ViewQuestion(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'base/question.html')


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contactus(name=name, email=email, message=message)
        contact.save()
        return redirect('/user')
    return render(request, 'users/contactus.html')

