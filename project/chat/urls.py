from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/(?P<search>\w+)/$', views.room, name='room'),
    url(r'^view/(?P<search>\w+)/$', views.view_detail, name='view_detail')
]