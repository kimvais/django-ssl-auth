from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^fi/?$', views.Fineid.as_view(), name='fi'),
    url(r'^$', views.Test.as_view(), name='home'),
]
