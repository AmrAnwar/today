from django.conf.urls import url

from .views import (
    AcceptWait,

)
urlpatterns = [
    url(r'^(?P<id>\d+)/accept/$', AcceptWait.as_view(), name="accept"),

]
