from django.conf.urls import patterns, url
from Admin import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/', views.register, name='register'),
        url(r'^login/', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/', views.logout, name='logout'),
        )