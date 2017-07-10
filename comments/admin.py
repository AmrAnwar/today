# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment


# Register your models here.
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['content', 'parent', 'timestamp', 'to_user', 'id']
    list_display_links = ['timestamp']
    list_filter = ['from_user', 'to_user', 'timestamp']


admin.site.register(Comment, admin_class=CommentModelAdmin)
