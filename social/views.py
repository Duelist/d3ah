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

def user_login(request,template_name='social/form.html'):
    username = ''
    password = ''
    forms = []
    errors = []
    
    if request.POST != None:
        forms.append(LoginForm(request.POST))
        errors.append('POST request')
        # Check validation of form list
#         if form.is_valid():
#             errors.append('Form is valid')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             
#             user = authenticate(username=username,password=password)
#             if user is not None:
#                 errors.append('User exists')
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponseRedirect(reverse(home_index))
#                 else:
#                     errors.append('User is not active in the system.')
#             else:
#                 errors.append('Incorrect user name or password has been entered.')
        return render_to_response(template_name,
                                  {'title': 'Login',
                                   'action': '/login/',
                                   'errors': errors,
                                   'forms': forms},
                                  context_instance=RequestContext(request))
    else:
        forms.append(LoginForm())
    
    return render_to_response(template_name,
                              {'errors': errors,
                               'forms': forms},
                              context_instance=RequestContext(request))

def registration(request,template_name='social/form.html'):
    username = ''
    password = ''
    errors = []
    
    if request.POST != None:
#         form = RegisterForm(request.POST)
#         errors.append('POST request')
#         if form.is_valid():
#             errors.append('Form is valid')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             
#             user = authenticate(username=username,password=password)
#             if user is not None:
#                 errors.append('User exists')
#                 if user.is_active:
#                     login(request,user)
#                     return HttpResponseRedirect(reverse(home_index))
#                 else:
#                     errors.append('User is not active in the system.')
#             else:
#                 errors.append('Incorrect user name or password has been entered.')
        return render_to_response(template_name,
                                  {'errors': errors,
                                   'form': form},
                                  context_instance=RequestContext(request))
    else:
        form = RegisterForm()
    
    return render_to_response(template_name,
                              {'errors': errors,
                               'form': form},
                              context_instance=RequestContext(request))

@login_required
def user_logout(request,template_name='social/index.html'):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def index(request,template_name='social/form.html'):
    pass

@login_required
def dashboard(request,template_name='social/dashboard.html'):
    errors = []
    
    return render_to_response(template_name,
                              {'errors':errors,
                               'user':request.user,
                               'profile': request.user.get_profile()},
                              context_instance=RequestContext(request))

@login_required
def profile(request,template_name='social/form.html'):
    forms = []
    errors = []
    #profile_form = None
    if request.POST:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            pass
    else:
        forms.append(UserForm(instance=request.user))
        forms.append(UserProfileForm(instance=UserProfile.objects.get(user=request.user)))
        
    return render_to_response(template_name,
                              {'title': 'My Profile',
                               'action': '/profile/',
                               'errors':errors,
                               'forms':forms},
                              context_instance=RequestContext(request))