from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from ..models import Post
from .serializers import PostSerializer
from likes.api.mixins import LikedMixin


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(
            body=self.request.data.get('body'),
            author=self.request.user
        )
