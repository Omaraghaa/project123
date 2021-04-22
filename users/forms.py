from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    number = forms.CharField()
    institute = forms.CharField()
    degree = forms.CharField()
    publications = forms.Field()
    funding = forms.CharField()
    type_of_funding = forms.CharField()
    patent = forms.CharField()
    license = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','number','institute','degree','publications','funding','type_of_funding','patent','license']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
