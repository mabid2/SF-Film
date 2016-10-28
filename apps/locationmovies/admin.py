from django.contrib import admin

# Register your models here.

from .models import Movies, Users

admin.site.register(Movies)
admin.site.register(Users)
