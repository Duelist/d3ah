from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from auctions.models import Auction

def index(request,template_name='auctions/index.html'):
    latest_auction_list = Auction.objects.all().order_by('-created_date')[:10]
    return render_to_response(template_name,context_instance=RequestContext(request))