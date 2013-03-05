from django.conf.urls.defaults import *

from social.views import *

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'social/login.html'}),
    (r'^logout/$', user_logout, {'template_name': 'social/index.html'}),
    (r'^profile/$', profile),
    (r'^register/$', registration),
)