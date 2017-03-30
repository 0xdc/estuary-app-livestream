from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^on_publish$', views.on_publish, name='on_publish'),
    url(r'^on_publish_done$', views.on_publish_done, name='on_publish_done'),
	url(r'^u/(?P<username>[a-z0-9]+)$', views.stream, name='stream'),
	url(r'^$', views.index, name='index'),
]
