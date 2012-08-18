from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_user(request,template_name='social/login.html'):
    username = ''
    password = ''
    errors = []
    
    if request.POST != None:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
    
    return render_to_response(template_name,{'errors': errors},context_instance=RequestContext(request))

@login_required
def profile(request,template_name='social/profile.html'):
    return render_to_response(template_name,context_instance=RequestContext(request))