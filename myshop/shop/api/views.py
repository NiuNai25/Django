from rest_framework import generics, viewsets,mixins
from ..models import Category, Product
from orders.models import Order,OrderItem
from .serializers import CategorySerializer,ProductSerializer,OrderSerializer,OrderItemSerializer  
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class CategoryAddView(generics.ListCreateAPIView):
     queryset =  Category.objects.all()
     serializer_class = CategorySerializer
     authentication_classes = (BasicAuthentication,)
     permission_classes = (IsAuthenticated,)

class  CategoryUpdateView(generics.UpdateAPIView ):
     queryset =  Category.objects.all()
     serializer_class = CategorySerializer
     authentication_classes = (BasicAuthentication,)
     permission_classes = (IsAuthenticated,)


class  CategoryDelete(generics.DestroyAPIView):
     queryset =  Category.objects.all()
     serializer_class = CategorySerializer
     authentication_classes = (BasicAuthentication,)
     permission_classes = (IsAuthenticated,)     

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class  ProductUpdateView(generics.UpdateAPIView ):
     queryset =  Product.objects.all()
     serializer_class = ProductSerializer
     authentication_classes = (BasicAuthentication,)
     permission_classes = (IsAuthenticated,)     

class OrderItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class OrderDelete(generics.DestroyAPIView):
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     authentication_classes = (BasicAuthentication,)
     permission_classes = (IsAuthenticated,)
