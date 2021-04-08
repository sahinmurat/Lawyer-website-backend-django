from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, request
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import Category, Comment,Post, Like, PostView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer, CommentSerializer
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwner

 
@api_view(['GET'])
@permission_classes([AllowAny])
def list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 200
    if request.method == 'GET':
        posts = Post.objects.filter(status = 'Published')
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many = True, context = {'request': request})
        return paginator.get_paginated_response(serializer.data)
    
    
