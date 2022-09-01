import email
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from base.models import Interviewee, Contactus

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ""
        self.fields['password2'].help_text = ""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)


class IntervieweeForm(forms.ModelForm):
    password = None
    category_name = None

    class Meta:
        model = Interviewee
        fields = ('category_name', 'client')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.TextInput(attrs={'class': 'form-control'})
        }

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