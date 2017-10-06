from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BookmarkListV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDetailV.as_view(), name='detail'),
    url(r'^create/$', BookmarkCreateV.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', BookmarkUpdateV.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', BookmarkDeleteV.as_view(), name='delete'),
]