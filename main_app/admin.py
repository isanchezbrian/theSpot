from django.contrib import admin

# Register your models here.
from .models import City, Post, Profile
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Post)
