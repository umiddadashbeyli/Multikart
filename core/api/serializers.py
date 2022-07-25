from rest_framework import serializers
from core.models import Basket, BasketItem
from product.api.serializers import ProductReadSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'username'
        )


class BasketReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # user = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Basket
        fields = (
            'id',
            'user',
        )

    # def validate(self, data):
    #     request = self.context['request']
    #     data['user'] = request.user
    #     return super().validate(data)


class BasketItemReadSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer()
    basket = BasketReadSerializer()
    class Meta:
        model = BasketItem
        fields = (
            'id',
            'basket',
            'product',
            'quantity'
        )


class BasketCreateSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Basket
        fields = (
            'id',
            # 'user',
        )

    # def validate(self, data):
    #     request = self.context['request']
    #     data['user'] = request.user
    #     return super().validate(data)


class BasketItemCreateSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(read_only = True)
    # basket = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = BasketItem
        fields = (
            'id',
            # 'basket',
            # 'product',
            # 'quantity'
        )

    # def validate(self, data):
    #     request = self.context['request']
    #     user = request.user
    #     print(request.user)
    #     data['product'] = request.data['product']
    #     data['basket'] = Basket.objects.filter(user = user).first() 
    #     return super().validate(data)