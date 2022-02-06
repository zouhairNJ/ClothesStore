from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'collections', views.CollectionViewSet)
router.register(r'promotions', views.PromotionViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'orderItem', views.OrderItemViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'cartItem', views.CartItemViewSet)


product_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls))
]
