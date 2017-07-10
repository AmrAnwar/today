from django.conf.urls import url

from .views import (
    account_detail,
    wait_list,
)
urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', account_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/wait/$', wait_list, name="wait"),

]
