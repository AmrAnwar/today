"""today URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import (
    home,
    logout_view,
    login_view,
    register_view,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^accounts/', include("allauth.urls")),

    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^comments/', include("comments.urls", namespace="comments")),
    url(r'^login/$', login_view, name="login"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^register/$', register_view, name="register"),
    url(r'^api/posts/', include("posts.api.urls", namespace='posts-api')),
    url(r'^api/accounts/', include("accounts.api.urls", namespace='accounts-api')),
    url(r'^$', home, name="home"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
