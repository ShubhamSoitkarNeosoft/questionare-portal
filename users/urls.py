from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homePage, name = 'home'),
    path('register/',views.registerUser , name = 'register'),
    path('login/', views.userLogin , name = 'login'),
    path('interviewee/', views.registerInterviewee , name='interviewee'),
]