from django.urls import path
from core.api.views import BasketAPI, BasketItemAPI, BasketReadUptadeDeleteAPI, BasketItemReadUptadeDeleteAPI


urlpatterns = [
    path('api/basket/', BasketAPI.as_view(), name="api_basket"),
    path('api/basket/<int:pk>/', BasketReadUptadeDeleteAPI.as_view(), name='basket_detail_api'),
    path('api/basket_item/', BasketItemAPI.as_view(), name="api_basket_item"),
    path('api/basket_item/<int:pk>/', BasketItemReadUptadeDeleteAPI.as_view(), name='basket_item_detail_api'),
]