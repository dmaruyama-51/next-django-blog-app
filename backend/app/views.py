from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics 
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostView(generics.ListAPIView):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 

class PostDetailView(generics.RetrieveAPIView):
    QuerySet = Post.objects.all()
    serializer_class = PostSerializer 