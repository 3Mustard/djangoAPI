from django.conf import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from AlbumApp import views

urlpatterns=[
    url(r'^group/$',views.groupApi),
    url(r'^group/([0-9]+)$',views.groupApi),

    url(r'^album/$',views.albumApi),
    url(r'^album/([0-9]+)$',views.albumApi),

    url(r'^saveFile$', views.saveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)