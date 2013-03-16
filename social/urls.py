from django.conf.urls.defaults import *

from social.views import *

urlpatterns = patterns('',
    (r'^login/$', user_login),
    (r'^logout/$', user_logout),
    (r'^profile/$', profile),
    (r'^register/$', registration),
    (r'^dashboard/$', dashboard),
)