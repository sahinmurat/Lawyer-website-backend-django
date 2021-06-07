from django.core import serializers
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, request
from django.core.serializers import serialize
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import  Comment,Post, Like, PostView
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
    
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def category(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)
    
    
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def categorycreate(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = 200
#     if request.method == 'POST':
#         print(request.data)
#         serializer = CategorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'message': 'it is created'
#             }
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    paginator = PageNumberPagination()
    paginator.page_size = 200
    if request.method == 'POST':
        print(request.data)
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            # category_serialize = Category(request.data['category'])
            # serializer.save(author=request.user,  category=category_serialize)
            data = {
                'message': 'it is created'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
   
 
@permission_classes([IsAuthenticated])
@api_view(["GET","POST"])
def detail_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    PostView.objects.create(author=request.user, post=post)
    if request.method == "POST":
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)
            data = {
                'message': 'Your comment is added'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = PostSerializer(post,  context = {'request': request})
        return Response(serializer.data)
    
 

@api_view(["PUT", "DELETE"])
@permission_classes([IsOwner, IsAuthenticated ])
def update_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "PUT":
        if request.user != post.author:
            return Response(
                {'message': 'You are not the owner of this post!'},  status=status.HTTP_403_FORBIDDEN
            )
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Post updated succesfully!"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        if request.user != post.author:
            data = {
               'message': 'You are not the owner of this post!'
            }
            return Response(data, status=status.HTTP_403_FORBIDDEN)
            
        post.delete()
        data = {
               'message': 'Your Post is successfully deleted!'
            }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(["POST"])   
def like(request, slug):
    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(author=request.user, post=obj)
        if like_qs:
            like_qs.delete()
            data = {
                'message': 'Your like is deleted'
            }
            # return Response( {'message': 'Your like  is deleted!'},status=status.HTTP_204_NO_CONTENT)
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            Like.objects.create(author=request.user, post=obj)
            data = {
                'message': 'Your like is succesfully taken!'
            }
            # return Response( {'message': 'Your like is succesfully taken!'},status=status.HTTP_204_NO_CONTENT)
            return Response(data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


    

 


