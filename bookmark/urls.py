from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', BookmarkListV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', BookmarkDetailV.as_view(), name='detail'),
]