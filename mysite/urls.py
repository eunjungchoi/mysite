"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from company import views


urlpatterns = [
    url(r'^loginform/$', views.loginform, name='loginform'),
    url(r'^login/$', views.log_in, name='login'),

    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signupform/$', views.signupform, name='signupform'),
    url(r'^signup/$', views.signup, name='signup'),


    url(r'^company/$', views.index, name='home'),
    url(r'^company/(?P<company_id>[0-9]+)$', views.company_detail),
    url(r'^company/news/$', views.news, name='news'),
    url(r'^company/news/(?P<news_id>[0-9]+)$', views.news_detail),
    
    url(r'^company/form/$', views.form, name='form'),
    url(r'^company/add/$', views.add, name='add'),
    url(r'^company/delete/(?P<company_id>[0-9]+)$', views.delete, name='delete'),
    url(r'^company/edit/$', views.edit, name='edit'),
    url(r'^company/editform/(?P<company_id>[0-9]+)$', views.editform, name='editform'),
    
    url(r'^company/addpeople/$', views.addpeople),
    url(r'^company/(?P<company_id>[0-9]+)/peopleform/$', views.peopleform, name='peopleform'),
    url(r'^company/deletepeople/(?P<people_id>[0-9]+)$', views.deletepeople, name='deletepeople'),
    url(r'^company/editpeople/(?P<people_id>[0-9]+)$', views.editpeople, name='editpeople'),
    url(r'^company/editp/$', views.editp, name='editp'),
    
    url(r'^company/jobs/$', views.jobs, name='jobs'),
    url(r'^company/jobs/(?P<jobs_id>[0-9]+)$', views.job_detail, name='jobdetail'),
    url(r'^company/(?P<company_id>[0-9]+)/jobform/$', views.jobform, name='jobform'),
    url(r'^company/addjob/$', views.addjob, name='addjob'),

    url(r'^people/', include('people.urls', namespace='people')),
    url(r'^company/position/', include('company.urls')),

    url(r'^hangout/', include('hangout.urls', namespace='hangout')),
    #url(r'^company/people/$', views.people, name='people'),
    #url(r'^company/people/(?P<people_id>[0-9]+)$', views.people_detail),


    url(r'^admin/', admin.site.urls)
]
