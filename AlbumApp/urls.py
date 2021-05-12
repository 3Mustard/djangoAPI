from django.conf.urls import url
from AlbumApp import views

urlpatterns=[
    url(r'^group/$',views.groupApi),
    url(r'^group/([0-9]+)$',views.groupApi)
]