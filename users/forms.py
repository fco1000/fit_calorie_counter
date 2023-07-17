from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import user

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = user
        fields = ['username','email']
        labels = ['Username','Email']
        
class UserchangeForm(UserChangeForm):
    class Meta:
        model = user
        fields = ['username','email']
        labels = ['Username','Email']