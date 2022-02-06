
from django.db.models.aggregates import Count
from ClothesStore.models import Cart, CartItem, Collection, Customer, Order, OrderItem, Product, Promotion, Review
from ClothesStore.serializers import CartItemSerializer, CartSerilaizer, CollectionSerializer, CustomerSerializer, OrderItemSerilaizer, OrderSerializer, ProductSerializer, PromotionSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [filters.SearchFilter]
    #filterset_fields = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']
    #permission_classes = [permissions.IsAdminUser]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        product_count=Count('products')).all()
    serializer_class = CollectionSerializer


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerilaizer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerilaizer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

     # get porduct_id from url
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
