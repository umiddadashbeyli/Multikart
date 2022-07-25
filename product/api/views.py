from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from product.models import Category, Product
from product.api.serializers import (CategoryReadSerializer, CategoryCreateSerializer,
                                    ProductReadSerializer, ProductCreateSerializer)
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from django.http import JsonResponse


class GenericAPIViewSerializerMixin:

    def get_serializer_class(self):
        return self.serializer_classes[self.request.method]


class CategoryAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Category.objects.all()
    permission_class = (IsAuthenticatedOrReadOnly)
    serializer_classes = {
        'GET' : CategoryReadSerializer,
        'POST' : CategoryCreateSerializer
    }


class ProductAPI(GenericAPIViewSerializerMixin, ListCreateAPIView):
    queryset = Product.objects.all()
    permission_class = (IsAuthenticatedOrReadOnly)
    serializer_classes = {
        'GET' : ProductReadSerializer,
        'POST' : ProductCreateSerializer
    }


class CategoryReadUptadeDeleteAPI(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_classes = {
        'GET' : CategoryReadSerializer,
        'PUT' : CategoryCreateSerializer,
        'PATCH' : CategoryCreateSerializer,
        'DELETE' : CategoryCreateSerializer
    }


class ProductReadUptadeDeleteAPI(GenericAPIViewSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_classes = {
        'GET' : ProductReadSerializer,
        'PUT' : ProductCreateSerializer,
        'PATCH' : ProductCreateSerializer,
        'DELETE' : ProductCreateSerializer
    }



# class CategoryAPI(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return super().get_serializer()
#         return CategoryReadSerializer


# class CategoryReadUptadeDeleteAPI(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategoryCreateSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return CategoryReadSerializer
#         return super().get_serializer()


# class CategoryAPI(APIView):

#     def get(self, request, *args, **kvargs):
#         categories = Category.objects.all()
#         serializer = CategoryReadSerializer(categories, context={'request' : request}, many = True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request, *args, **kvargs):
#         form_data = request.data
#         serializer = CategoryCreateSerializer(data=form_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False, status = 201)
#         return JsonResponse(serializer.errors, safe=False, status = 400)

# class CategoryReadUptadeDeleteAPI(APIView):
#     def get_object(self, pk):
#         if self.request.method == "GET":
#             try:
#                 return Category.objects.get(pk=pk)
#             except Category.DoesNotExist:
#                 raise Http404

    
#     def get(self, pk):
#         category = self.get_object(pk)
#         serializer = CategoryReadSerializer(category)
#         return Response(serializer.data)


#     def put(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategoryCreateSerializer(instance=category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, pk):
#         category = Category.objects.get(pk=pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

#     def patch(self, request, pk):
#         category = Category.objects.get(pk=pk)
#         serializer = CategoryCreateSerializer(data=request.data, partial=True, instance=category)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)