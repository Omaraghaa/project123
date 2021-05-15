from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=30)
    institute = forms.CharField(max_length=30)
    degree = forms.CharField()
    publications = forms.Field()
    funding = forms.CharField()
    type_of_funding = forms.CharField()
    patent = forms.CharField()
    license = forms.CharField()

    class Meta:
        model = User
        fields = [ 'username',
                   'email',
                   'phone_number',
                   'institute',
                   'degree',
                   'publications',
                   'funding',
                   'type_of_funding',
                   'patent','license',
                   'password1', 
                   'password2'
                 ]#'number','institute','degree','publications','funding','type_of_funding','patent','license'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
 
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
# Creating user profile form fields
class UserProfileForm(forms.ModelForm):
    class Meta:
      model = UserProfile
      fields = [ 'phone_number',
                 'institute',
                 'degree',
                 'publications',
                 'funding',
                 'type_of_funding',
                 'patent','license'
                ]

