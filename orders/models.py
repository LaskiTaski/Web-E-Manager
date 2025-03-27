from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]

    table_number = models.IntegerField(verbose_name="Номер стола")
    items = models.JSONField(verbose_name="Список блюд")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость", default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")

    # Автоматический расчет общей суммы
    def save(self, *args, **kwargs):
        self.total_price = sum(item.get('price', 0) for item in self.items)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} - Стол {self.table_number} ({self.get_status_display()})"
