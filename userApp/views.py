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
    c = RequestContext(request)

    c.update(csrf(request))
    if request.GET:
        if 'next' in request.GET:
            c['next'] = request.GET.get('next')
    # state = "Please Login"
    state = ""
    username = password = ''

    # redirect the user if already logged in
    if request.user.is_authenticated():
        if request.GET.get('next') != None:
            return HttpResponseRedirect(request.GET.get('next'))
        else:
            return HttpResponseRedirect('/')

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
                    if request.POST['next'] != '' and request.POST['next'] != None:
                        return HttpResponseRedirect(request.POST['next'])
                    else:
                        return HttpResponseRedirect('/')
            else:
                state="Invalid Email Address or Password."
    else:
        form = UserForm()
    c['state'] = state
    c['form'] = form
    return render_to_response("userApp/login.html", c)



def register(request):
    c = RequestContext(request)
    c.update(csrf(request))
    state = ""
    username = password = ''

    # redirect the user if already logged in
    if request.user.is_authenticated():
        if request.GET.get('next') != None:
            return HttpResponseRedirect(request.GET.get('next'))
        else:
            return HttpResponseRedirect('/')
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                User.objects.create_user(username, username, password)
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
                myUser.set_password(form.cleaned_data['password'])
                myUser.save()
                logoutUser(request)
                return HttpResponseRedirect('/')
            except:
                return HttpResponse("An error occurred please try again.")
    return render_to_response('userApp/profile.html', c)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

