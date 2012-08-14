from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from nhlwishlist.apps.account.models import UserProfile
from nhlwishlist.apps.account.forms import LoginForm, RegisterForm


def register_user(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            dupe_email = User.objects.filter(email__iexact=form.cleaned_data['email_address'])
            
            confirmed_passwords = form.cleaned_data['password'] == form.cleaned_data['password_confirmation']
            
            
            if dupe_email:
                pass
            elif not confirmed_passwords:
                pass
            else:
                user = User.objects.create_user(form.cleaned_data['username'],form.cleaned_data['email_address'], form.cleaned_data['password'])
                profile = UserProfile(user=user)
                profile.save()
                
                return redirect('home')
                
    else:
        form = RegisterForm()
        
        
    return render(request, 'account/register.html', {'form': form})
    
    
def user_login(request):
    
    next = request.GET.get('next')
    if next == None:
        next = 'home'

    if request.method == "POST":
        
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            # Valid user.
            if user is not None:
                login(request, user)
                next = request.POST["next"]
                
                
                if next:
                    return redirect(next)
                else:
                    return redirect('home')

            
            else:
                pass

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form, 'next': next})
    
def user_logout(request):
    
    logout(request)
    
    return redirect('home')