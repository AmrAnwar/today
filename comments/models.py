# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, reverse

User = get_user_model()


# Create your models here.
class Comment(models.Model):
    from_user = models.ForeignKey(User, null=False, default=False, related_name="comment_sender")
    to_user = models.ForeignKey(User, default=False, related_name="comment_receiver")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.IntegerField(null=False)
    likes = models.ManyToManyField(User, blank=True, related_name="comments_like")

    class Meta:
        ordering = ['-timestamp']

    def get_like_url(self):
        return reverse("comments:like", kwargs={"id": self.id})
