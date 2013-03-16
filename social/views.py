from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from social.forms import *
from social.models import AppUser

def user_login(request,template_name='social/form.html'):
    username = ''
    password = ''
    forms = []
    errors = []
    
    if request.POST:
        forms.append(LoginForm(request.POST))
        # Wankery below:
        # forms_valid = reduce(lambda x,y: x and y, map(lambda x: x.is_valid(), forms))
        if forms[0].is_valid():
            username = forms[0].cleaned_data.get('username')
            password = forms[0].cleaned_data.get('password')
            
            user = authenticate(username=username,password=password)
            if user:
                errors.append(user)
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse(dashboard))
                else:
                    errors.append('User is not active in the system.')
            else:
                errors.append('Incorrect user name or password has been entered.')
        else:
            errors.append('Username or password is invalid.')
        return render_to_response(template_name,
                                  {'title': 'Login',
                                   'action': '/login/',
                                   'button_text': 'Login',
                                   'errors': errors,
                                   'forms': forms},
                                  context_instance=RequestContext(request))
    else:
        forms.append(LoginForm())

    return render_to_response(template_name,
                              {'title': 'Login',
                               'action': '/login/',
                               'button_text': 'Login',
                               'errors': errors,
                               'forms': forms},
                              context_instance=RequestContext(request))

def registration(request,template_name='social/form.html'):
    username = ''
    password = ''
    forms = []
    errors = []
    
    if request.POST:
        forms.append(RegistrationForm(request.POST))

        if forms[0].is_valid():
            username = forms[0].cleaned_data.get('username')
            email = forms[0].cleaned_data.get('email')
            password = forms[0].cleaned_data.get('password')

            user = AppUser(username=username, email=email)
            user.set_password(password)
            user.save()
            # send_mail('Registration complete.',
            #           'Registration complete.',
            #           'admin@d3ah.example',
            #           [email],
            #           fail_silently=False)
            return HttpResponseRedirect(reverse(home_index))
        return render_to_response(template_name,
                                  {'title': 'Register',
                                   'action': '/register/',
                                   'button_text': 'Register',
                                   'errors': errors,
                                   'forms': forms},
                                  context_instance=RequestContext(request))
    else:
        forms.append(RegistrationForm())

    return render_to_response(template_name,
                              {'title': 'Register',
                               'action': '/register/',
                               'button_text': 'Register',
                               'errors': errors,
                               'forms': forms},
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

    if request.POST:
        forms.append(AppUserForm(request.POST))
        if forms[0].is_valid():
            email = forms[0].cleaned_data.get('email')
            password = forms[0].cleaned_data.get('password')

            user = AppUser.objects.get(username=request.user.username)
            user.email = email
            user.set_password(password)
            user.save()
            return HttpResponseRedirect(reverse(home_index))
        return render_to_response(template_name,
                                  {'title': 'My Profile',
                                   'action': '/profile/',
                                   'button_text': 'Save',
                                   'errors':errors,
                                   'forms':forms},
                                  context_instance=RequestContext(request))
    else:
        data = {'email':request.user.email,
                'password':' ',
                'password_confirm':' '}
        forms.append(AppUserForm(data))

    return render_to_response(template_name,
                              {'title': 'My Profile',
                               'action': '/profile/',
                               'button_text': 'Save',
                               'errors':errors,
                               'forms':forms},
                              context_instance=RequestContext(request))

@login_required
def dashboard(request,template_name='social/dashboard.html'):
  # Create auctions, view existing auctions, profile edit
  return render_to_response(template_name,
                            {},
                            context_instance=RequestContext(request))