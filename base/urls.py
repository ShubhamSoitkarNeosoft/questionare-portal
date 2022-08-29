from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.AddQuestion, name='question'),
    path('viewquestion/<question_id>', views.ViewQuestion, name='viewquestion'),
]