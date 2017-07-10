# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import RedirectView
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, reverse
from django.contrib.auth import get_user_model
from posts.models import Post


# Create your views here.
class AcceptWait(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            post = get_object_or_404(Post, id=self.kwargs.get("id"))
            if post.to_user == self.request.user:
                post.wait = False
                post.save()
                return reverse("accounts:wait", kwargs={"slug": post.to_user.username})
        else:
            return reverse("/")

