from .models import Post
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict


class PostAPIView(APIView):
    def get(self, request):
        p = Post.objects.all()
        return Response({'post': PostSerializer(p, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_new = Post.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': PostSerializer(post_new).data})
