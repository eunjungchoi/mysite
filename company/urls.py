from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.position, name='position'),
    url(r'^(?P<position_name>[\w\-]+)/$', views.byposition, name='byposition'),
]