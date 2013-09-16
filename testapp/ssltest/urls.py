from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from . import views

urlpatterns = patterns('',
    url(r'^$', views.Main.as_view(), name='home'),
)
