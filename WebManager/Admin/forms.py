from django import forms
from django.contrib.auth.models import User
from Admin.models import Employee

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    hash = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password')