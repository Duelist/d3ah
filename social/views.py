from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from branding.views import index as home_index
from social.forms import *
from social.models import *

def user_login(request,template_name='social/login.html'):
    username = ''
    password = ''
    errors = []
    
    if request.POST != None:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse(home_index))
    else:
        form = LoginForm()
    
    return render_to_response(template_name,{'errors': errors, 'form': form},context_instance=RequestContext(request))

@login_required
def user_logout(request,template_name='social/index.html'):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def index(request,template_name='social/login.html'):
    pass

@login_required
def profile(request,template_name='social/profile.html'):
    errors = []
    #profile_form = None
    if request.POST != None:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            pass
    else:
        user_form = UserForm(instance=request.user)
        #profile = UserProfile.objects.get(user=request.user)
        profile_form = UserProfileForm()
        
    return render_to_response(template_name, {'errors':errors, 'user_form':user_form, 'profile_form': profile_form}, context_instance=RequestContext(request))