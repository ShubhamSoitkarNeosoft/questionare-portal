from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Question, QuestionSet, Assignment, Technology
from ckeditor.widgets import CKEditorWidget


class QuestionForm(forms.ModelForm):
    question = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = ['question', 'technology', 'client', 'category']


class TechForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['technology_name']


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"

