from django.contrib import admin

# Register your models here.

from .models import Favorites, Movies, Users

admin.site.register(Favorites)
admin.site.register(Movies)
admin.site.register(Users)
