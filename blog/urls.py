from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	
]