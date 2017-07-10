# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'timestamp', 'from_user', 'to_user', 'id']
    list_display_links = ['timestamp']
    # list_editable = ['content']
    list_filter = ['from_user', 'to_user', 'timestamp']


admin.site.register(Post, admin_class=PostModelAdmin)
