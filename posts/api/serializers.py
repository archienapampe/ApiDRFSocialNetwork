from rest_framework import serializers

from ..models import Post
from likes import services as likes_services


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'body',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj):
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

    def create(self, validated_data):
        post = Post.objects.create(
            body=validated_data.get('body'),
            author=validated_data.get('author')
        )
        return post
