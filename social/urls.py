from django.conf.urls.defaults import *

from social.views import *

urlpatterns = patterns('',
    url(r'^login/$', user_login),
    url(r'^logout/$', user_logout),
    url(r'^profile/$', profile),
    url(r'^register/$', registration),
    url(r'^dashboard/$', dashboard),
    url(r'^dashboard/(?P<page_name>[-\w]+)/$', dashboard, name='social_dashboard'),
)