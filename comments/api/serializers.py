from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from comments.models import Comment
from accounts.api.serializers import UserDetailOnlySerializer

class CommentSerializer(ModelSerializer):
    likes = SerializerMethodField()
    class Meta:
        model = Comment
        fields = [
            'id',
            'from_user',
            'to_user',
            'parent',
            'content',
            'timestamp',
            'likes',
        ]
    def get_likes(self,obj):
        like_users = obj.likes.all()
        return UserDetailOnlySerializer(like_users, many=True).data
