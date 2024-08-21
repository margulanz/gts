from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status, viewsets


from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    
    serializer_class = PostSerializer
    lookup_field = 'slug'
    http_method_names = ['get']
    def get_queryset(self):
        queryset = Post.objects.all().order_by('-pub_date')

        tags = self.request.query_params.getlist('tags', None)
        category = self.request.query_params.get('category', None)
        keywords = self.request.query_params.get('keywords', None)

        if tags:
            tags_q = Q()
            for tag in tags:
                tags_q |= Q(tags__name__iexact=tag)
            queryset = queryset.filter(tags_q).distinct()

        if category:
            queryset = queryset.filter(category__name=category)

        if keywords:
            queryset = queryset.filter(
                Q(title__icontains=keywords) | 
                Q(content__icontains=keywords)
            )

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        tags = request.query_params.get("tags")
        category = request.query_params.get("category")
        keywords = request.query_params.get("keywords")

        if tags or category or keywords:
            post_links = [
                reverse('posts-detail', args=[post.slug], request=request)
                for post in queryset
            ]
            return Response(post_links)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)