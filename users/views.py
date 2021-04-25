from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from linkedin import linkedin
from urllib import parse
import requests
from django.http import HttpResponse, HttpResponseRedirect


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def linkedin_auth(request):
    CLIENT_KEY = '861nbok5ugrdlw'
    CLIENT_SECRET = 'qwuPM1VEc5Uyzrwx'
    RETURN_URL = 'http://127.0.0.1:8000/register/'

    authentication = linkedin.LinkedInAuthentication(
                    CLIENT_KEY,
                    CLIENT_SECRET,
                    RETURN_URL,
                    ['r_liteprofile', 'r_emailaddress']
                )

    authorization_url = authentication.authorization_url

    #res = requests.get(authorization_url, allow_redirects=True)
    #url_ = res.url
    return HttpResponseRedirect(authorization_url)

def linkedin_usr_info(request):
    CLIENT_KEY = '861nbok5ugrdlw'
    CLIENT_SECRET = 'qwuPM1VEc5Uyzrwx'
    RETURN_URL = 'http://127.0.0.1:8000/register/'

    
    url_ = request.build_absolute_uri()
    #print('Ninad',url_s)
    parsed_url = dict(parse.parse_qsl(parse.urlsplit(url_).query))
    print(parsed_url)
    parsed_url_ = dict(parse.parse_qsl(parse.urlsplit(parsed_url['r']).query))
    print('Ninad', parsed_url_)
    code_ = parsed_url_['code']
    print('nnnnn', code_)
    authentication = linkedin.LinkedInAuthentication(
                    CLIENT_KEY,
                    CLIENT_SECRET,
                    RETURN_URL,
                    ['r_liteprofile', 'r_emailaddress']
                )

    authentication.authorization_code = code_
    token_ = authentication.get_access_token()
    print('tttttt',token_.access_token)
    application = 'https://api.linkedin.com/v2/me?oauth2_access_token=' + token_.access_token

    res = requests.get(application)
    res_json = res.json()
    fname = res_json['localizedFirstName']
    lname = res_json['localizedLastName']
    
    context = {
        'f_name': fname,
        'l_name': lname,
        'return': 'y'
    }


    # if request.method == 'POST':
    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Your account has been created! You are now able to log in')
    #         return redirect('login')
    # else:
    form = UserRegisterForm()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.username = '12134324231'
        instance.save()
        # form.fields["username"].initial = fname + lname
        # form.save()   

    return render(request, 'users/register.html', {'form': form, 'y': 1})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
