
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Question, QuestionSet, Assignment, Technology
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Csv , Question,Mentor,Category, QuestionSet,Contactus,Technology,Assesment,Client,Interviewee 
from ckeditor.widgets import CKEditorWidget


class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = ['question', 'technology', 'client', 'category']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"


class TechForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['technology_name']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interviewee
        fields = ['user', 'client', 'interview_date', 'category_name']
    

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
    

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = "__all__"
        

class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields="__all__"           