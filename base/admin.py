from django.contrib import admin
from .models import Client, Mentor , Interviewee, Category, QuestionSet, Question

admin.site.register(Client)
admin.site.register(Mentor)
admin.site.register(Category)
admin.site.register(QuestionSet)
admin.site.register(Question)

class IntervieweeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'client']

admin.site.register(Interviewee, IntervieweeAdmin)
