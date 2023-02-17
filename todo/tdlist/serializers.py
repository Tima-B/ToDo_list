from rest_framework import serializers
from tdlist.models import Tasklist


class TasklistSerializer(serializers.ModelSerializer):
    """Сериализатор по модели Tasklist."""

    # article_comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # article_comments = CommentSerializer(many=True)
    # author = serializers.CharField(source='author.username', default=None)
    # author = UserSerializer()

    # image = Base64ImageField()

    class Meta:
        model = Tasklist
        read_only_fields = ["id", "created_time", "finish_time"]
        fields = "__all__"
