from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Cart, CartItem, Collection, Customer, Order, OrderItem, Product, Promotion, Review


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name',
                  'email', 'phone', 'birth_date', 'membership']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'unit_price', 'Stock', 'last_update', 'promotions'
                  ]


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'featured_product', 'product_count']

    product_count = serializers.IntegerField(read_only=True)


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['description', 'discount'
                  ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['Order_time', 'payment_status', 'customer']


class OrderItemSerilaizer(serializers.ModelSerializer):
    product = ProductSerializer

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'unit_price']


class CartSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'created_at']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
