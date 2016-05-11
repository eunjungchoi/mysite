from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.people, name='index'),
    url(r'^(?P<people_id>[0-9]+)$', views.people_detail, name="detail"),
]
