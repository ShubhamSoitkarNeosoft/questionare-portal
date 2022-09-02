from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.AddQuestion, name='question'),
    path('viewquestion', views.ViewQuestion, name='viewquestion'),
    path('result/', views.ViewResult, name='result'),
    path('assign/', views.AssignView, name='assign'),

]