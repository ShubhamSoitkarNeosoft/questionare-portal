from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from .forms import QuestionForm, TechForm, ClientForm, InterviewForm, CategoryForm, MentorForm, AssignmentForm
from .models import Question, Contactus, Category
from django.contrib.auth import authenticate, get_user_model, login, logout
from base.models import Client, Question, Technology, Assignment, Interviewee, Assesment, Mentor
from users.forms import IntervieweeForm


def AddQuestion(request):
    form = QuestionForm()
    try:
        client = request.session['client']
        category = request.session['category_name']
    except:
        form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('question')
    return render(request, 'base/addquestion.html', {'form': form, 'client1': client, 'category': category})


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
            #user.save()
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


def admin(request):
  question = Question.objects.count()
  contact = Contactus.objects.count()
  interview = Interviewee.objects.count()
  client = Client.objects.count()
  mentor = Mentor.objects.count()
  category = Category.objects.count()
  assesment = Assesment.objects.count()
  assignment = Assignment.objects.count()
  technology = Technology.objects.count()
  return render(request, 'admin.html', {'question': question, 'contact': contact, 'interview': interview, 'client': client, 'mentor': mentor, 'category': category, 'assesment': assesment, 'assignment': assignment,'technology':technology})


def contact_table(request):  
    contact = Contactus.objects.all()
    question = Question.objects.all()
    return render(request, 'base/contacttable.html', {'contact':contact, 'question': question})


def ques_table(request):  
    question = Question.objects.all()
    return render(request, 'base/qatable.html', {'question': question})


def client_table(request):
    client = Client.objects.all()
    return render(request, 'base/clienttable.html', {'client': client})


def interview_table(request):
    inter = Interviewee.objects.all()
    return render(request, 'base/interviewtable.html', {'inter': inter})


def category_table(request):
    category = Category.objects.all()
    return render(request, 'base/categtable.html', {'category': category})


def assesment_table(request):
    assesment = Assesment.objects.all()
    return render(request, 'base/assestable.html', {'assesment': assesment})


def mentor_table(request):
    mentor = Mentor.objects.all()
    return render(request, 'mentortable.html', {'mentor': mentor})


def technologytable(request):
    technology = Technology.objects.all()
    return render(request, 'base/techtable.html', {'technology': technology})


def addcateg(request):   
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        
    return render(request, 'base/addcateg.html', {'form': form})


def addmentor(request):
    form = MentorForm()
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addmentor')
    return render(request, 'base/addmentor.html', {'form': form})


def admintech(request):
    form = TechForm()
    if request.method == 'POST':
        form = TechForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_technology')
    return render(request, 'base/admintech.html', {'form': form})


def addclient(request):   
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/addclient.html', {'form': form})


def addinterview(request):   
    intform = InterviewForm()
    if request.method == 'POST':
        intform = InterviewForm(request.POST)  
        print(intform)
        if intform.is_valid():
            intform.save()
        return redirect('addint')
    return render(request, 'base/addinterview.html', {'intform': intform})


def UserAssignView(request):
    form = AssignmentForm()
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('assignuser')
    return render(request, 'base/assignuser.html', {'form': form})


def Assignment_table(request):
    assign = Assignment.objects.all()
    return render(request, 'base/assigntable.html', {'assign': assign})



