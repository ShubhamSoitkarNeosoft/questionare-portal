from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.AddQuestion, name='question'),
    path('viewquestion', views.ViewQuestion, name='viewquestion'),
    path('result/', views.ViewResult, name='result'),
    path('assign/', views.AssignView, name='assign'),
 	path('addcategory/',views.addcateg,name='addcate'),
    path('addmentor/',views.addmentor,name='addmentor'),
    path('add_technology/', views.admintech, name='adminq'),
    path('admin/',views.admin,name='admin'),
    path('viewquestion/<question_id>', views.ViewQuestion, name='viewquestion'),
    path('contable/',views.contact_table,name='ctable'),
    path('qatable/',views.ques_table,name='qatable'),
    path('clienttable/',views.client_table,name='client'),
    path('intertable/',views.interview_table,name='itable'),
    path('categtable/',views.category_table,name='catetable'),
    path('assestable/',views.assesment_table,name='asstable'),
    path('mentortable/',views.mentor_table,name='mentortable'),
 path('client/', views.addclient, name='clientadd'),
path('interviewee/',views.addinterview,name='addint'),
 


   
]