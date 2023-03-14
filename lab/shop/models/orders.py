from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(
        to='shop.Product',
        related_name='orders',
        blank=True,
    )
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Имя')
    phone = models.CharField(max_length=100, null=False, blank=False, verbose_name='Телефон')
    address = models.CharField(max_length=300, null=False, blank=False, verbose_name='Адрес')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
