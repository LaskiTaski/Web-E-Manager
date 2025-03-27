from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для Order: автоматически рассчитывает total_price
    """
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_items(self, value):
        # Проверяем, что каждый элемент — словарь с 'name' и 'price'
        if not isinstance(value, list):
            raise serializers.ValidationError("Список блюд должен быть списком объектов.")
        for item in value:
            if not isinstance(item, dict):
                raise serializers.ValidationError("Каждый элемент должен быть словарём.")
            if 'name' not in item or 'price' not in item:
                raise serializers.ValidationError("Каждое блюдо должно содержать 'name' и 'price'.")
        return value
