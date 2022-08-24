from django.contrib import admin
from base.models import Client, Mentor , Interviewee

admin.site.register(Client)

admin.site.register(Mentor)


class IntervieweeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'client']

admin.site.register(Interviewee, IntervieweeAdmin)
