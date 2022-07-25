from django.urls import path
from . import views
from product.views import ProductListView, ProductDetailView, CartListView

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart'),
    path('products/', ProductListView.as_view(), name='category'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('search/', views.search, name='search'),
    path('vendor/', views.vendor, name='vendor'),
    # path('update_item/', views.updateItem, name='update_item'),
]