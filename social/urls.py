from django.conf.urls.defaults import *

from social.views import *

urlpatterns = patterns('',
    (r'^login/', login_user),
    (r'^profile/$', profile),
)