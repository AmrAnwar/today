from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)
from comments.api.serializers import CommentSerializer

from comments.models import Comment
from posts.models import Post
from accounts.api.serializers import UserDetailOnlySerializer

post_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='id',
)
post_delete_url = HyperlinkedIdentityField(
    view_name='posts-api:delete',
    lookup_field='id',
)
class PostCreateUpdateSerializer(ModelSerializer):
    from_user = UserDetailOnlySerializer(read_only=True)
    to_user = UserDetailOnlySerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'from_user',
            'to_user',
            'content',
        ]

class PostDetailSerializer(ModelSerializer):
    comments = SerializerMethodField()
    from_user = UserDetailOnlySerializer(read_only=True)
    to_user = UserDetailOnlySerializer(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'from_user',
            'to_user',
            'content',
            'comments',
        ]
    def get_comments(self, obj):
        # content_type = obj.get_content_type
        # object_id = obj.id
        comments = Comment.objects.filter(parent = obj.id)
        return CommentSerializer(comments, many=True).data


class PostListSerializer(ModelSerializer):
    from_user = UserDetailOnlySerializer(read_only=True)
    to_user = UserDetailOnlySerializer(read_only=True)
    url = post_url
    delete_url = post_delete_url

    class Meta:
        model = Post
        fields = [
            'url',
            'from_user',
            'to_user',
            'content',
            'timestamp',
            'delete_url'
        ]