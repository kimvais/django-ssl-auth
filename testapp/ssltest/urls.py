from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from . import views

urlpatterns = patterns('',
    url(r'^fi/?$', views.Fineid.as_view(), name='fi'),
    url(r'^$', views.Test.as_view(), name='home'),
)
