
from django.contrib import messages
from django.core.mail import send_mail
from django.core import serializers
from django.shortcuts import render, redirect, HttpResponse
from users.forms import CustomUserCreationForm, IntervieweeForm, ContactForm, AssesmentForm
from django.contrib.auth import authenticate, get_user_model, login, logout
from base.models import Client, Question, Technology
from base.forms import QuestionForm
import json
from base.models import Contactus
from django.contrib.auth import logout


def homePage(request):
    return render(request, 'index.html')


def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('login')
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        request.session['user'] = str(user)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                login(request, user)
                return redirect('admin')
            return redirect('assign')
        else:
            print("user is not authenticated")
    return render(request, 'users/login.html')


def registerInterviewee(request):
    form = IntervieweeForm()
    if request.method == 'POST':
        form = IntervieweeForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            client = form.cleaned_data['client']
            request.session['client'] = str(client)
            category = form.cleaned_data['category_name']
            request.session['category_name'] = str(category)
            print(request.session['category_name'])
            return redirect('question')
    return render(request, 'users/interviewee.html', {'form': form})


def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contactus(name=name, email=email,message=message)
        contact.save()
        print("hello")
        messages.success(request, "Query registered Succesfully!!")
    # return redirect ('/user/contact')
    return render(request, 'users/contactus.html')


def UserDashboardView(request):
    user = request.user
    return render(request, 'users/dashboard.html', {'user': user})


def assesment(request):
    form = AssesmentForm()
    if request.method == 'POST':
        print(request.POST)
        form = AssesmentForm(request.POST)
        if form.is_valid():
            print(form.is_valid)
            form.save()
    return render(request, 'users/assesment.html', {'form': form})


