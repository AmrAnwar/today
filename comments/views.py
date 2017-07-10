# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404, redirect, reverse
from .models import Comment

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class CommentLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        comment_id = self.kwargs.get("id")
        print (comment_id)
        comment = get_object_or_404(Comment, id=comment_id)
        # profile_instance = get_object_or_404(User, user=comment.to_user)
        # url_ = profile_instance.get_absolute_url()
        user = self.request.user
        if user.is_authenticated():
            pass
            if user in comment.likes.all():
                comment.likes.remove(user)
            else:
                comment.likes.add(user)
        else:
            return reverse("/")
        return reverse("accounts:detail", kwargs={"slug": comment.to_user.username})
