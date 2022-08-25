from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from users.forms import CustomUserCreationForm, IntervieweeForm
from django.contrib.auth import authenticate,get_user_model,login,logout


def homePage(request):
    return render(request, 'index.html')


def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'users/register.html', {'form':form})


def userLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('interviewee')
        else:
            print("user is not authenticated")
    return render(request, 'users/login.html')


def registerInterviewee(request):
    form  = IntervieweeForm()
    if request.method == 'POST':
        form = IntervieweeForm(request.POST)
        if form.is_valid():
            # print('--------',form.instance.user)
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            print('----',user.user)
            return redirect('login')
    return render(request, 'users/interviewee.html', {'form':form})


