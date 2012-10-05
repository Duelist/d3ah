from django.conf.urls.defaults import *

from auctions.views import *

urlpatterns = patterns('',
    (r'^auctions/$', index),
)