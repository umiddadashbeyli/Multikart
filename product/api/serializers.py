from rest_framework import serializers
from product.models import Category, Product, Tag, Brand, PropertyValue


class ParentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent_category'
        )


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            'id',
            'title',
        )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'tag',
        )


class PropertyValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyValue
        fields = (
            'id',
            'title',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent_category'
        )     


class CategoryCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent_category'
        )


class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    tags = TagSerializer(source = 'get_tags', many = True)
    property_values = PropertyValueSerializer(source = 'get_property_values', many = True)

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'brand',
            'property_values',
            'category',
            'main_image',
            'description',
            'detail',
            'video',
            'tags'
        )

    
class ProductCreateSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(read_only = True)

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'brand',
            'property_value',
            'category',
            'main_image',
            'description',
            'detail',
            'video',
            'tags'
        )

    # def validate(self, data):
    #     request = self.context['request']
    #     data['author'] = request.user
    #     return super().validate(data)


class CategoryReadSerializer(serializers.ModelSerializer):
    products = ProductReadSerializer(source = 'get_products', many = True)
    parent_category = ParentCategorySerializer()
    

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent_category',
            'products'
        )