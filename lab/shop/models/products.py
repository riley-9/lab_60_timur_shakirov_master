from django.db import models
from django.db.models import TextChoices


class CategoryChoices(TextChoices):
    OTHER = 'other', 'Разное'
    COMPUTERS = 'computers', 'Компьютеры'
    NOTEBOOKS = 'notebooks', 'Ноутбуки'
    MOBILE_PHONES = 'mobile_phones', 'Мобильные телефоны'
    TOYS = 'toys', 'Игрушки'
    FURNITURE = 'furniture', 'Мебель'


class Product(models.Model):
    product = models.CharField(max_length=100, null=False, blank=False, verbose_name='Продукт')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    photo = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Фото')
    category = models.CharField(
        max_length=100,
        choices=CategoryChoices.choices,
        null=False,
        blank=False,
        default=CategoryChoices.OTHER, verbose_name='Категория')
    rest = models.IntegerField(null=False, blank=False, verbose_name='Остаток')
    price = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2, verbose_name='Стоимость')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f"Продукт: {self.product}  |  Категория: {self.get_category_display()}  |  Стоимость: {self.price}  |  "

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
