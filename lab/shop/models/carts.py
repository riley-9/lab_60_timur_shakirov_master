from django.db import models


class Cart(models.Model):
    product = models.ForeignKey(
        to='shop.Product',
        verbose_name='Продукт',
        related_name='carts',
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(null=False, blank=False, verbose_name='Количество')

    @staticmethod
    def add_to_cart(cart_products, main_product):
        if main_product in [cart_product.product for cart_product in cart_products]:
            cart_product = cart_products.get(product_id=main_product.pk)
            if main_product.rest > cart_product.amount:
                cart_product.amount += 1
                cart_product.save()
        else:
            cart = Cart()
            if main_product.rest > 0:
                cart.product = main_product
                cart.amount = 1
                cart.save()

    @staticmethod
    def get_total(cart):
        if cart:
            total = 0
            for product in cart:
                total += product.product.price * product.amount
            return total

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
