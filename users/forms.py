from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    institute = forms.CharField(max_length=30)
    degree = forms.CharField()
    Number_of_publications = forms.IntegerField()
    funding = forms.IntegerField()
    type_of_funding = forms.CharField()
    Number_of_patents = forms.IntegerField()
    license = forms.CharField()
    Project_title = forms.CharField()
    Project_details = forms.CharField( widget=forms.Textarea)
    class Meta:
        model = User
        fields = [ 'username',
                   'email',
                   'password1', 
                   'password2',
                   'phone_number',
                   'institute',
                   'degree',
                   'Number_of_publications',
                   'Number_of_patents',
                   'license',
                   'Project_title',
                   'Project_details',
                   'funding',
                   'type_of_funding',
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
                 'Number_of_publications',
                 'funding',
                 'type_of_funding',
                 'Number_of_patents','license',
                 'Project_title',
                   'Project_details'
                ]

