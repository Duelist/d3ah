from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from auctions.models import Auction

def index(request,template_name='auctions/index.html'):
    auctions = Auction.objects.filter(type='hc')
    return render_to_response(template_name, {'auctions': auctions},
                              context_instance=RequestContext(request))