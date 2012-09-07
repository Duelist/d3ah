from django.conf.urls.defaults import *

from social.views import *

urlpatterns = patterns('',
    (r'^login/', 'django.contrib.auth.views.login', {'template_name': 'social/login.html'}),
    (r'^profile/$', profile),
)