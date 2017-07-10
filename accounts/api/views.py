from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.filters import SearchFilter, OrderingFilter


from posts.models import Post,Comment
from .serializers import (
    UserDetailSerializer,
)
from django.contrib.auth import (
    get_user_model,


)
User = get_user_model()

class UserDetailAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    # lookup_url_kwarg = "abc"
