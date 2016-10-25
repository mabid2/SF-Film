from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact$', views.contact),
    url(r'^login$', views.login),
    url(r'^register$', views.registerUser),
    url(r'^signin$', views.loginUser)
]
