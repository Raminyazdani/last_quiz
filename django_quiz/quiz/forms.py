from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    fullname = forms.CharField(max_length=200,required=False)

    class Meta:
        model = User
        fields = ('fullname', 'username', 'password1', 'password2', )

class verifyForm():
    verify_code = forms.CharField(max_length=30)

