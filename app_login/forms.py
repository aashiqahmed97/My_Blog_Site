from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from .models import userProfile

class signUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required =True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class UserProfileChange (UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password']

class profilePic(ModelForm) :
    class Meta:
        model = userProfile
        fields = ['profile_picture']
        




