from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('', include('guestbookapp.urls')),
)
