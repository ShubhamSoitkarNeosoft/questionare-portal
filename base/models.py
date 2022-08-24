from django.db import models
from django.contrib.auth import get_user_model


class Mentor(models.Model):
    name = models.CharField(max_length=255)
    assigned_date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    interview_date = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    status = models.BooleanField()
    mentor = models.ForeignKey(Mentor, on_delete= models.PROTECT)

    def __str__(self):
        return f'{self.name}'

class Interviewee(get_user_model()):
    user = models.OneToOneField(get_user_model(), on_delete= models.PROTECT, related_name='+')
    client = models.ForeignKey(Client , on_delete = models.PROTECT)
    interview_date = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user}'
