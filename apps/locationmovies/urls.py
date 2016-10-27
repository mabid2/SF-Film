from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact$', views.contact),
    url(r'^login$', views.login),
    url(r'^register$', views.registerUser),
    url(r'^signin$', views.loginUser),
    url(r'^search$', views.search),
    url(r'^display$', views.display),
    url(r'^displayAll$', views.displayAll),
    url(r'^search$', views.search),
    # url(r'^addFav$', views.addWishlist),
    # url(r'^wishlist$', views.displayWishlist)

]
