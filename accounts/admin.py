from django.contrib import admin
from .models import Profile
# Register your models here.


class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(Profile, UserProfileModelAdmin)