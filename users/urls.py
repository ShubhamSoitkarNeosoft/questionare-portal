from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.userLogin, name='login'),
    path('interviewee/', views.registerInterviewee, name='interviewee'),
    path('contact/', views.contactus, name='contact'),
    path('logout/', views.logout_view,  name="logout"),
    path('dashboard/', views.UserDashboardView,  name="dashboard"),
 path('assesment/',views.assesment,name='assesment'),
]