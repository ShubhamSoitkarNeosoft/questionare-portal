from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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
    mentor = models.ForeignKey(Mentor, on_delete=models.PROTECT)
    requirement_id = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Technology(models.Model):
    Technology_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Technology_name


class Interviewee(get_user_model()):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    interview_date = models.CharField(max_length=255)
    Technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.user}'


class QuestionSet(models.Model):
    Interviewee = models.ForeignKey(Interviewee, on_delete=models.CASCADE)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.Client} '


class Question(models.Model):
    Technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    question = models.TextField()
    Question_set = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'

