from django.urls import path
from .views import ProductListAPIView, ProductCountAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/count/', ProductCountAPIView.as_view(), name='product-count'),
]
