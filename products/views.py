from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 5              # items per page
    page_size_query_param = 'page_size'
    max_page_size = 50

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class ProductCountAPIView(APIView):
    """Returns the total count of products."""
    def get(self, request, *args, **kwargs):
        count = Product.objects.count()
        return Response({'count': count})
