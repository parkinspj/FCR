#urls.py - URL patterns for Guestbook App
from django.conf.urls.defaults import *

urlpatterns = patterns('guestbookapp.views',
                       url(r'^$', 'home', name='guestbook_home'),
)