from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from auctions.forms import SearchForm
from auctions.models import Auction

def index(request,template_name='auctions/index.html'):
    auctions = Auction.objects.filter(type='hc').order_by('-created_date')[:10]
    search_form = SearchForm()
    return render_to_response(template_name, 
                             {'auctions': auctions, 'search_form':search_form, 'user':request.user},
                             context_instance=RequestContext(request))
