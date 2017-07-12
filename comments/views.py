# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404, redirect, reverse
from .models import Comment

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
# class CommentLikeToggle(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         comment_id = self.kwargs.get("id")
#         print (comment_id)
#         comment = get_object_or_404(Comment, id=comment_id)
#         user = self.request.user
#         url = '/'
#         if user.is_authenticated():
#             pass
#             if user in comment.likes.all():
#                 comment.likes.remove(user)
#             else:
#                 comment.likes.add(user)
#         else:
#             return url
#         url = reverse("accounts:detail", kwargs={"slug": comment.to_user.username})
#         return url


class CommentLikeApiToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, format=None):
        print "LOL"
        comment = get_object_or_404(Comment, id=id)
        print comment
        user = self.request.user
        url = reverse("accounts:detail", kwargs={"slug": comment.to_user.username})
        updated = False
        liked = False
        if user.is_authenticated():
            if user in comment.likes.all():
                liked = False
                comment.likes.remove(user)
            else:
                liked = True
                comment.likes.add(user)
            updated = True
        # else:
        #     url = '/'
        count = comment.likes.count()
        data = {
            "updated": updated,
            "liked": liked,
            'id': comment.id,
            'counted': count,
        }
        return Response(data)
