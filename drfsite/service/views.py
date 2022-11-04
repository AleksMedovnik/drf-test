from .models import Post, Category
from .serializers import PostSerializer, CatSerializer
from rest_framework import generics, viewsets


class CatViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class PostAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDestroy(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
