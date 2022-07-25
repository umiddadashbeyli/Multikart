from django.urls import path
from product.api.views import CategoryAPI, CategoryReadUptadeDeleteAPI, ProductAPI, ProductReadUptadeDeleteAPI


urlpatterns = [
    path('api/category/', CategoryAPI.as_view(), name="api_category"),
    path('api/category/<int:pk>/', CategoryReadUptadeDeleteAPI.as_view(), name='category_detail_api'),
    path('api/product/', ProductAPI.as_view(), name="api_product"),
    path('api/product/<int:pk>/', ProductReadUptadeDeleteAPI.as_view(), name='product_detail_api'),
]