from .models import Post
from rest_framework import generics
from .serializers import PostSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict

'''class PostAPIView(APIView):
    def get(self, request):
        lst = Post.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Post.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})
        instance.title = request.data['title']
        instance.content = request.data['content']
        instance.cat_id = request.data['cat_id']
        instance.save()
        return Response({'post': request.data})


class PostDelete(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        Post.objects.get(pk=pk).delete()
        return Response({'post': f'Delete post {str(pk)}'})'''

'''class PostAPIView(APIView):
    def get(self, request):
        l = Post.objects.all()
        return Response({'post': PostSerializer(l, many=True).data})

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method put not allowed'})
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response({'error': 'Object not...'})
        serializer = PostSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})'''
