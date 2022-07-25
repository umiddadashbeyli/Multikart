from venv import create
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from core.api.serializers import (BasketItemReadSerializer, BasketReadSerializer,
                                    BasketCreateSerializer, BasketItemCreateSerializer, User)
from core.models import Basket, BasketItem
from product.models import Product
from rest_framework import status
from rest_framework.response import Response


class GenericAPIViewSerializerMixin:

    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


class BasketAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Basket.objects.all()
    permission_class = (IsAuthenticatedOrReadOnly)
    serializer_classes = {
        'GET' : BasketReadSerializer,
        'POST' : BasketCreateSerializer
    }

    def post(self, request, *args, **kwargs):
        userID = request.data.get('userID')
        basket, created = Basket.objects.get_or_create(user = request.user)
        return Response(userID, status=status.HTTP_200_OK)


class BasketItemAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = BasketItem.objects.all()
    permission_class = (IsAuthenticatedOrReadOnly)
    serializer_classes = {
        'GET' : BasketItemReadSerializer,
        'POST' : BasketItemCreateSerializer
    }

    def post(self, request, *args, **kwargs):
        productID = request.data.get('productID')
        action = request.data.get('action')
        quantity = request.data.get('quantity')
        product = Product.objects.filter(pk = productID).first()
        basket = Basket.objects.filter(user = request.user).first()
        basketItem, created = BasketItem.objects.get_or_create(product = product, basket = basket)

        

        if action == 'add':
            basketItem.quantity += int(quantity)
        elif action == 'remove':
            basketItem.quantity -= (quantity)

        basketItem.save()

        if basketItem.quantity <= 0:
            basketItem.delete()

        return Response(productID, status=status.HTTP_200_OK)


class BasketReadUptadeDeleteAPI(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_classes = {
        'GET' : BasketReadSerializer,
        'PUT' : BasketCreateSerializer,
        'PATCH' : BasketCreateSerializer,
        'DELETE' : BasketCreateSerializer
    }


class BasketItemReadUptadeDeleteAPI(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = BasketItem.objects.all()
    serializer_classes = {
        'GET' : BasketItemReadSerializer,
        'PUT' : BasketItemCreateSerializer,
        'PATCH' : BasketItemCreateSerializer,
        'DELETE' : BasketItemCreateSerializer
    }