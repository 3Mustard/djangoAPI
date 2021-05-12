from django.conf.urls import url
from AlbumApp import views

urlspatterns=[
    url(r'^group/$',views.GroupApi),
    url(r'^group/([0-9]+)$',views.GroupApi)
]