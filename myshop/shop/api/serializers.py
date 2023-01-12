from rest_framework import serializers
from ..models import Category,Product
from orders.models import Order,OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class ProductSerializer(serializers.ModelSerializer):
    Category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','category', 'name', 'slug', 'description', 'price', 'stock', 'created', 'updated', 'Category')

class OrderItemSerializer(serializers.ModelSerializer):
    Product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = OrderItem
        fields = ('id','price', 'order_id','product_id', 'Product')    


class OrderSerializer(serializers.ModelSerializer):
    OrderItem = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('id','first_name', 'last_name', 'OrderItem')        


