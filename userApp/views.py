from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django import forms
from django.template import RequestContext

class UserForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus':'autofocus', 'placeholder':'Email Address'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)

class ProfileForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, max_length=100)

# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    # state = "Please Login"
    state = ""
    username = password = ''
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            myuser = None
            myuser = authenticate(username=username, password=password)
            if myuser is not None:
                if myuser.is_active:
                    auth_login(request, myuser)
                    return HttpResponseRedirect('/projects')
            else:
                state="Invalid Email Address or Password."
    else:
        form = UserForm()
    c['state'] = state
    c['form'] = form
    return render_to_response("userApp/login.html", c)



def register(request):
    c = {}
    c.update(csrf(request))
    state = ""
    username = password = ''
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                User.objects.create_user(username, username, password)
                # return HttpResponse('You have successfully created your account. Please <a href="/user/login">login</a>')
                return HttpResponseRedirect("/projects")
            state = "Email address already exists. Please Login or use another Email address"
    else:
        form = UserForm()
    c['form'] = form
    c['state'] = state
    return render_to_response('userApp/signup.html', c)

def profile(request):
    c = RequestContext(request)
    c['form'] = ProfileForm()
    if request.POST:
        form = ProfileForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            try:
                myUser = User.objects.get(username=request.user)
            except:
                return HttpResponse("An error occurred please try again.")
            print myUser
    return render_to_response('userApp/profile.html', c)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/projects")

