from django.urls import reverse
from django.views.generic import CreateView

from shop.forms.orders import OrderForm
from shop.models import Cart, Order, OrderProductAmount


class OrderAddView(CreateView):
    template_name = 'orders/add_order.html'
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        cart_products = Cart.objects.all()
        order = form.save()
        for cart_product in cart_products:
            form.instance.products.add(cart_product.product)
            amount = OrderProductAmount.objects.create(order_id=order.pk,
                                                       product=cart_product.product,
                                                       order_amount=cart_product.amount)
        cart_products.delete()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main')
