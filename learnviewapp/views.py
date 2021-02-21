from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,CreateAPIView,DestroyAPIView
from learnviewapp.serializers import PostMediaSerializer
from learnviewapp.models import PostMedia

class PostCreateAPIView(CreateAPIView):
    queryset = PostMedia.objects.all()
    serializer_class =  PostMediaSerializer

class PostListAPIView(ListAPIView):
    queryset = PostMedia.objects.all()
    serializer_class = PostMediaSerializer
   