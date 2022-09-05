from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
User = get_user_model()


class Mentor(models.Model):
    name = models.CharField(max_length=255)
    assigned_date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    category_name = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.category_name}'


class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    interview_date = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    status = models.BooleanField()
    mentor = models.ForeignKey(Mentor, on_delete=models.PROTECT)
    requirement_id = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'


class Technology(models.Model):
    technology_name = models.CharField(max_length=50)

    def __str__(self):
        return self.technology_name


class Interviewee(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='+')
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    interview_date = models.DateField(max_length=255, null=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    # def __str__(self):
    #     return f'{self.user}'


class Question(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.question}'


class QuestionSet(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} {self.Client} '


class Contactus(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=20)
    message = models.TextField(blank=True, null=True)


status = (
    ("Selected", "Selected"),
    ("Rejected", "Rejected"),
    ("Waiting for feedback", "Waiting for feedback"),
    ("Waiting for Kickstart", "Waiting for Kickstart"),
    ("Waiting for schedule", "Waiting for schedule"),
    ("Assigned", "Assigned"),
)


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    job_description = models.CharField(max_length=1000)
    job_profile = models.CharField(max_length=1000)
    assigned_date = models.CharField(max_length=1000)
    assigned_by = models.CharField(max_length=1000)
    status = models.CharField(max_length=255, choices=status)

    def __str__(self):
        return f'{self.status}'


class Assesment(models.Model):
    user = models.ManyToManyField(User, blank=True)
    question = RichTextField(blank=True, null=True)
    year_of_experience = models.IntegerField()


class Csv(models.Model):
    file_name=models.FileField(upload_to='csv')
    def __str__(self):
        return f'{self.file_name}'