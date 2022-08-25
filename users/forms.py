import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from base.models import Interviewee

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)






class IntervieweeForm(UserChangeForm):
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    password = None
    class Meta:
        model = Interviewee
        fields = ('Technology', 'client')

# class UserLoginForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email',)
#     # email = forms.CharField(help_text=False)
    # password = forms.CharField()

    # def clean(self, *args, **kwargs):
    #     username = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')

    #     if username and password:
    #         user = authenticate(username=username,password=password)
    #         if not user:
    #             raise forms.ValidationError('User Does Not Exist')
    #         if not user.check_password(password):
    #             raise forms.ValidationError('Incorrect Password')
    #     return super(UserLoginForm, self).clean(*args, **kwargs)