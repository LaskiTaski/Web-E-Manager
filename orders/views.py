from django.shortcuts import render
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления заказами.
    Позволяет выполнять CRUD-операции:
    - создание заказа (POST)
    - просмотр списка заказов и отдельного заказа (GET)
    - обновление заказа (PUT/PATCH)
    - удаление заказа (DELETE)
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



def index(request):
    return render(request, 'orders/index.html')
