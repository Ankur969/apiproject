from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

class PostPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-id')  # Order by most recent
    serializer_class = PostSerializer
    pagination_class = PostPagination
