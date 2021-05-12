from django.conf.urls import url
from AlbumApp import views

urlpatterns=[
    url(r'^group/$',views.groupApi),
    url(r'^group/([0-9]+)$',views.groupApi),
    url(r'^album/$',views.albumApi),
    url(r'^album/([0-9]+)$',views.albumApi)
]