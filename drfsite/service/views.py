from .models import Post
from .serializers import PostSerializer
from rest_framework import generics


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDestroy(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
