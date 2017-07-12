from django.conf.urls import url

from .views import (
    # CommentLikeToggle,
    CommentLikeApiToggle,
)
urlpatterns = [

    # url(r'^(?P<id>\d+)/like/$', CommentLikeToggle.as_view(), name="like"),
    url(r'^api/(?P<id>\d+)/like/$', CommentLikeApiToggle.as_view(), name="like-api"),

]
