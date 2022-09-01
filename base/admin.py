from django.contrib import admin
from .models import Client, Mentor , Interviewee, Technology, QuestionSet, Question, Category, Contactus, Assignment

admin.site.register(Client)
admin.site.register(Mentor)
admin.site.register(Technology)
admin.site.register(QuestionSet)
admin.site.register(Category)


class IntervieweeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'client']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['client', 'technology', 'question', 'category']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Interviewee, IntervieweeAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(Contactus, ContactAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['client', 'user', 'status', 'job_profile', 'assigned_date', 'assigned_by']

admin.site.register(Assignment, AssignmentAdmin)