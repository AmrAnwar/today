from django.conf.urls import url

from .views import (
    account_detail,
    wait_list,
    account_edit,
)
urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', account_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/wait/$', wait_list, name="wait"),
    url(r'^(?P<slug>[\w-]+)/edit/$', account_edit, name="edit"),

]
