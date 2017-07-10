from django.conf.urls import url

from .views import (
    CommentLikeToggle,
)
urlpatterns = [
    url(r'^(?P<id>\d+)/like/$', CommentLikeToggle.as_view(), name="like"),

]
