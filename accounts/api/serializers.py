from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField,
)
from comments.models import Comment
from posts.models import Post

User = get_user_model()
class UserDetailSerializer(ModelSerializer):
    posts = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'posts',

        ]
    def get_posts(self,obj):
        posts = Post.objects.filter(to_user=obj)
        return PostDetailSerializer(posts, many=True).data


class PostDetailSerializer(ModelSerializer):
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'id',
            'from_user',
            'content',
            'comments',
        ]
    def get_comments(self, obj):
        comments = Comment.objects.filter(parent = obj.id)
        return CommentSerializer(comments, many=True).data

class CommentSerializer(ModelSerializer):
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