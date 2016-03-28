from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^posts/$', views.post_list, name='post_list'),
	url(r'^$', views.query_new, name='query_new'),
	url(r'^about/$', views.about, name='about'),
	url(r'^result/(?P<pk>\d+)/$', views.results, name='results'),
	
]