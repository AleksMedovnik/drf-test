from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class PostAPIView(APIView):
    def get(self, request):
        p = Post.objects.all()
        return Response({'posts': PostSerializer(p, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *argsl, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        Post.objects.get(pk=pk).delete()
        return Response({'post': f'Delete post {str(pk)}'})
