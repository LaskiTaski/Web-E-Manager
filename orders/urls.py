from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, index

# Создаём роутер и регистрируем ViewSet
router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', index, name='orders_home'),
]
