from django.conf.urls.defaults import *
from branding.views import *

urlpatterns = patterns('',
    (r'^$', index, {'template_name': 'branding/index.html'}),
)