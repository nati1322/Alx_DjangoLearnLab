from django.shortcuts import render
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

User = get_user_model()

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(recipient=post.author, actor=request.user, verb='liked your post', target=post)
            return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Post already liked'}, status=status.HTTP_200_OK)

class UnlikePostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        post = Post.objects.get(pk=self.kwargs['pk'])
        try:
            like = Like.objects.get(post=post, user=request.user)
            like.delete()
            return Response({'message': 'Post unliked'}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({'message': 'Post not liked'}, status=status.HTTP_400_BAD_REQUEST)
