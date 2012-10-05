from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def index(request,template_name='branding/index.html'):
    return render_to_response(template_name, context_instance=RequestContext(request))