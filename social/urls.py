from django.conf.urls.defaults import *

from social.views import *

urlpatterns = patterns('',
    (r'^login/$', user_login, {'template_name': 'social/login.html'}),
    (r'^logout/$', user_logout, {'template_name': 'social/index.html'}),
    (r'^profile/$', profile),
)