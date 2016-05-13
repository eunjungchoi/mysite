from django.conf.urls import patterns, url
from hangout import views

urlpatterns = patterns('', 
	url(r'^$', views.HangoutModelView.as_view(), name='index'),

	url(r'^place/$', views.PlaceList.as_view(), name='place_list'),
	url(r'^city/$', views.CityList.as_view(), name='city_list'),
	url(r'^category/$', views.CategoryList.as_view(), name='category_list'),
	url(r'^visit/$', views.VisitList.as_view(), name='visit_list'), 

	url(r'^place/(?P<pk>\d+)/$', views.PlaceDetail.as_view(), name='place_detail'),
	url(r'^city/(?P<pk>\d+)/$', views.CityDetail.as_view(), name='city_detail'),
	url(r'^category/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name='category_detail'), 
	url(r'^visit/(?P<pk>\d+)/$', views.VisitDetail.as_view(), name='visit_detail')
)