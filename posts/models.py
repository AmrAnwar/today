# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from comments.models import Comment
User = get_user_model()


# Create your models here.

class Post(models.Model):
    from_user = models.ForeignKey(User, null=False, default=False, related_name="sender")
    to_user = models.ForeignKey(User, default=False, related_name="receiver")
    content = models.TextField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    wait = models.BooleanField(default=True)
    # likes = models.ManyToManyField(User, blank=True, related_name="posts_likes")
    class Meta:
        ordering = ["-timestamp"]

    def __unicode__(self):
        return "%s:%s%s" % (self.from_user, self.to_user, self.id)

    def get_comments(self):
        return Comment.objects.filter(parent=self.id)