from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact$', views.contact),
    url(r'^login$', views.login),
    url(r'^register$', views.registerUser),
    url(r'^signin$', views.loginUser),
    url(r'^search$', views.search),
    url(r'^displayAll$', views.displayAll),
    url(r'^search$', views.search),
    # url(r'^addFavorite$', views.addWishlist),
    url(r'^deleteFav$', views.deleteWishlist),
    url(r'^display/(?P<id>\d+)$', views.display),
    url(r'^logout$', views.logout),
    url(r'^wishlist$', views.wishlist),
    url(r'^displayapes$', views.displayapes),
    url(r'^displaysan$', views.displaysan),
    url(r'^displayharry$', views.displayharry),
    url(r'^displayvertigo$', views.displayvertigo),
    # url(r'^wishlist$', views.displayWishlist)

]
